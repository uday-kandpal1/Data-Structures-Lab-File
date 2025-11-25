class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
# Singly Linked List class
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    # Function to insert a node at the end
    def insert_end(self, data):
        new_node = Node(data)
        # If list is empty
        if self.head is None:
            self.head = new_node
            return
        # Traverse to the last node
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    # Function to delete node at the beginning
    def delete_begin(self):
        if self.head is None:
            print("List is empty. Cannot delete.")
            return
        print(f"Deleting node at beginning: {self.head.data}")
        self.head = self.head.next
    # Function to delete node at the end
    def delete_end(self):
        if self.head is None:
            print("List is empty. Cannot delete.")
            return
        # If only one node exists
        if self.head.next is None:
            print(f"Deleting last node: {self.head.data}")
            self.head = None
            return
        # Traverse to the second last node
        temp = self.head
        while temp.next.next:
            temp = temp.next
        print(f"Deleting node at end: {temp.next.data}")
        temp.next = None
    # Function to print the linked list
    def display(self):
        if self.head is None:
            print("List is empty.")
            return
        temp = self.head
        print("Linked List:", end=" ")
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
# Main Program
if __name__ == "__main__":
    sll = SinglyLinkedList()
    # Insert sample data
    sll.insert_end(10)
    sll.insert_end(20)
    sll.insert_end(30)
    sll.insert_end(40)
    print("\nInitial List:")
    sll.display()
    print("\nDeleting from beginning:")
    sll.delete_begin()
    sll.display()
    print("\nDeleting from end:")
    sll.delete_end()
    sll.display()
