class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None
        
class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtStart(self, data):
        if self.head is None:
            self.head = Node(data)
            self.head.prev = self.head
            self.head.next = self.head
            return
        new_node = Node(data)
        new_node.next = self.head
        self.head.prev = new_node
        # self.head = new_node
        node = self.head
        while(node.next != self.head):
            node = node.next
        node.next = new_node
        new_node.prev = node
        self.head = new_node
        
    def insertAtEnd(self, data):
        new_node = Node(data)
        new_node.next = self.head
        node = self.head
        if self.head is None:
            self.insertAtStart(data)
            return
        while(node.next != self.head):
            node = node.next
        new_node.prev = node
        node.next = new_node
        
    def insertAfterItem(self, val, data):
        present = self.search(val)
        if not present:
            print(val, "element is not present in the linked list which you are trying to remove")
            return
        new_node = Node(data)
        node = self.head
        while(node.next != None):
            if node.data == val:
                break
            node = node.next
        new_node.next = node.next
        new_node.prev = node
        node.next = new_node
        
    def insertBeforeItem(self, val, data):
        present = self.search(val)
        if not present:
            print(val, "element is not present in the linked list which you are trying to remove")
            return
        if self.head.data == val:
            self.insertAtStart(data)
            return
        new_node = Node(data)
        node = self.head
        previous_node = None
        while(node.next != None):
            if node.data == val:
                break
            previous_node = node
            node = node.next
        new_node.prev = node.prev
        new_node.next = node
        node.prev = new_node
        previous_node.next = new_node
        
    def deleteAtFirst(self):
        if self.head is None:
            return
        node = self.head
        print("Deleted item :", self.head.data)
        while(node.next != self.head):
            node = node.next
        self.head = self.head.next
        self.head.prev = node
        node.next = self.head
        
    def deleteAtEnd(self):
        if self.head is None:
            return
        node = self.head
        previous = None
        while(node.next != self.head):
            previous = node
            node = node.next
        previous.next = self.head
        self.head.prev = previous
        
    def deleteItem(self, val):
        present = self.search(val)
        if not present:
            print(val, "element is not present in the linked list which you are trying to remove")
            return
        if val == self.head.data:
            self.deleteAtFirst()
            return
        previous_node = None
        node = self.head
        while(node.next != self.head):
            if node.data == val:
                print("Deleted item :", node.data)
                previous_node.next = node.next
                node.next.prev = previous_node
                return
            previous_node = node
            node = node.next
        print("Deleted item :", node.data)
        previous_node.next = self.head
        self.head.prev = previous_node
            
    def print_linked_list(self):
        if self.head is None:
            return
        print("-"*100)
        node = self.head
        while(node.next != self.head):
            print(node.data, end="\t")
            node = node.next
        print(node.data, end="\n")
        print("-"*100)
        
    def search(self, val):
        if self.head is None:
            return false
        node = self.head
        found = False
        while(node.next != self.head):
            if node.data == val:
                break
            node = node.next
        if node.data == val:
            found = True
        return found
    
    def length(self):
        if self.head is None:
            return 0
        counter = 1
        node = self.head
        while(node.next != self.head):
            counter += 1
            node = node.next
        return counter
    
    def reverseLinkedList(self):
        previous_node = None
        current_node = self.head
        next_node = self.head.next
        while(current_node.next != self.head):
            current_node.next = previous_node
            current_node.prev = next_node
            previous_node = current_node
            current_node = next_node
            next_node = next_node.next
        current_node.next = previous_node
        current_node.prev = self.head
        self.head.next = current_node
        self.head = current_node
        
cdll = CircularDoublyLinkedList()

print("Inserting 40 at the start of the linked list".center(100," "), end="\n\n")
cdll.insertAtStart(40)
cdll.print_linked_list()

print("Inserting 25 at the start of the linked list".center(100," "), end="\n\n")
cdll.insertAtStart(25)
cdll.print_linked_list()

print("Inserting 50 at the end of the linked list".center(100," "), end="\n\n")
cdll.insertAtEnd(50)
cdll.print_linked_list()

print("Inserting 20 at the start of the linked list".center(100," "), end="\n\n")
cdll.insertAtStart(20)
cdll.print_linked_list()

print("Inserting 35 after 30 in the linked list".center(100," "), end="\n\n")
cdll.insertAfterItem(25, 35)
cdll.print_linked_list()

print("Inserting 30 after 25 in the linked list".center(100," "), end="\n\n")
cdll.insertAfterItem(25, 30)
cdll.print_linked_list()

print("Inserting 45 before 50 in the linked list".center(100," "), end="\n\n")
cdll.insertBeforeItem(50, 45)
cdll.print_linked_list()

print("Inserting 32 before 35 in the linked list".center(100," "), end="\n\n")
cdll.insertBeforeItem(35, 32)
cdll.print_linked_list()

print("Removing first element from the linked list".center(100," "), end="\n\n")
cdll.deleteAtFirst()
cdll.print_linked_list()

print("Removing Last element from the linked list".center(100," "), end="\n\n")
cdll.deleteAtEnd()
cdll.print_linked_list()

print("Removing 32 element from the linked list".center(100," "), end="\n\n")
cdll.deleteItem(32)
cdll.print_linked_list()

present = cdll.search(40)
print("Element present in the linked list :", present)
present = cdll.search(70)
print("Element present in the linked list :", present)

length = cdll.length()
print('Length of the Linked list :', length)

print('Reversing the linked list'.center(100,'-'))
cdll.reverseLinkedList()
cdll.print_linked_list()