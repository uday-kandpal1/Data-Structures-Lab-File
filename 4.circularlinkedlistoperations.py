class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
# Circular Singly Linked List
class CircularLinkedList:
    def __init__(self):
        self.head = None
    # Insert at BEGINNING
    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            new_node.next = new_node
            self.head = new_node
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        new_node.next = self.head
        temp.next = new_node
        self.head = new_node
    # Insert at END
    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            new_node.next = new_node
            self.head = new_node
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head
    # SEARCH for a value
    def search(self, key):
        if self.head is None:
            print("List is empty")
            return False
        temp = self.head
        while True:
            if temp.data == key:
                print("Found:", key)
                return True
            temp = temp.next
            if temp == self.head:
                break
        print("Not Found:", key)
        return False
    # DELETE from BEGINNING
    def delete_from_beginning(self):
        if self.head is None:
            print("List is empty")
            return
        # Only one node
        if self.head.next == self.head:
            print("Deleting:", self.head.data)
            self.head = None
            return
        # Find last node
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        print("Deleting:", self.head.data)
        temp.next = self.head.next
        self.head = self.head.next
    def delete_from_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next == self.head:
            print("Deleting:", self.head.data)
            self.head = None
            return
        prev = None
        temp = self.head
        while temp.next != self.head:
            prev = temp
            temp = temp.next
        print("Deleting:", temp.data)
        prev.next = self.head
    def display(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(Back to head)")
cll = CircularLinkedList()
cll.insert_at_beginning(10)
cll.insert_at_beginning(20)
cll.insert_at_end(30)
cll.insert_at_end(40)
cll.display()
cll.search(30)
cll.search(100)
cll.delete_from_beginning()
cll.display()
cll.delete_from_end()
cll.display()