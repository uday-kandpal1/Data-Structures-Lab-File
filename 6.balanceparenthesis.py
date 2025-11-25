# Function to check balanced parentheses
def is_balanced(expression):
    stack = []
    opening = "([{"
    closing = ")]}"
    # Mapping closing → opening
    pair = {')': '(', ']': '[', '}': '{'}
    for ch in expression:
        # If opening bracket → push to stack
        if ch in opening:
            stack.append(ch)
        # If closing bracket → check stack top
        elif ch in closing:
            if not stack:
                return False
            if stack.pop() != pair[ch]:
                return False
    # Balanced if stack is empty at end
    return len(stack) == 0
# ---- USER INPUT ----
expr = input("Enter an expression with brackets: ")
if is_balanced(expr):
    print("Balanced")
else:
    print("Not Balanced")
