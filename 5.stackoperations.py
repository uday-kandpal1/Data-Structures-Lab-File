# STACK OPERATIONS (Menu Driven)
stack = []
def push():
    item = input("Enter item to push: ")
    stack.append(item)
    print(f"Pushed {item}")
def pop_item():
    if not stack:
        print("Stack is empty.")
    else:
        popped = stack.pop()
        print(f"Popped {popped}")
def peek():
    if not stack:
        print("Stack is empty.")
    else:
        print(f"Top item is {stack[-1]}")
def display():
    if not stack:
        print("Stack is empty.")
    else:
        print("Stack items:", stack)
# POSTFIX EXPRESSION EVALUATION
# Function to perform arithmetic operations
def apply_operation(op1, op2, operator):
    if operator == '+':
        return op1 + op2
    elif operator == '-':
        return op1 - op2
    elif operator == '*':
        return op1 * op2
    elif operator == '/':
        return op1 // op2   # integer division
    else:
        raise ValueError("Invalid Operator!")
# Function to evaluate postfix expression
def evaluate_postfix(expression):
    stack = []
    tokens = expression.split()        # split by spaces
    for token in tokens:
        if token.isdigit():            # number → push to stack
            stack.append(int(token))
        else:                          # operator → pop two values
            op2 = stack.pop()
            op1 = stack.pop()
            result = apply_operation(op1, op2, token)
            stack.append(result)
    return stack.pop()                 # final answer
# MAIN MENU
while True:
    print("\n===== STACK MENU =====")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Evaluate Postfix Expression")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        push()
    elif choice == "2":
        pop_item()
    elif choice == "3":
        peek()
    elif choice == "4":
        display()
    elif choice == "5":
        expr = input("Enter a postfix expression (space separated): ")
        try:
            result = evaluate_postfix(expr)
            print("Result =", result)
        except Exception as e:
            print("Error evaluating expression:", e)
    elif choice == "6":
        print("Exiting program.")
        break
    else:
        print("Invalid choice, please try again.")