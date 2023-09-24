class Node:
    def __init__(self, data=None):
        self.prev = None
        self.next = None
        self.data = data
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    def insertAtStart(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        
    def insertAtEnd(self, data):
        if self.head is None:
            self.insertAtStart(data)
            return
        new_node = Node(data)
        node = self.head
        while(node.next != None):
            node = node.next
        node.next = new_node
        new_node.prev = node
        
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
        self.head = self.head.next
        self.head.prev = None
        
    def deleteAtEnd(self):
        if self.head is None:
            return
        node = self.head
        previous = None
        while(node.next != None):
            previous = node
            node = node.next
        previous.next = None
        
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
        while(node.next != None):
            if node.data == val:
                break
            previous_node = node
            node = node.next
        previous_node.next = node.next
        node.prev = previous_node
        
    def print_linked_list(self):
        if self.head is None:
            return
        print("-"*100)
        node = self.head
        while(node != None):
            print(node.data, end="\t")
            node = node.next
        print()
        print("-"*100)
        
    def search(self, val):
        node = self.head
        found = False
        while(node != None):
            if node.data == val:
                found = True
                break
            node = node.next
        return found
            
    def length(self):
        counter = 0
        node = self.head
        while(node != None):
            counter += 1
            node = node.next
        return counter
    
    def reverseLinkedList(self):
        previous_node = None
        current_node = self.head
        next_node = self.head.next
        while(current_node.next != None):
            current_node.next = previous_node
            current_node.prev = next_node
            previous_node = current_node
            current_node = next_node
            next_node = next_node.next
        current_node.next = previous_node
        current_node.prev = None
        self.head = current_node
                
dll = DoublyLinkedList()

print("Inserting 40 at the start of the linked list".center(100," "), end="\n\n")
dll.insertAtStart(40)
dll.print_linked_list()

print("Inserting 25 at the start of the linked list".center(100," "), end="\n\n")
dll.insertAtStart(25)
dll.print_linked_list()

print("Inserting 50 at the end of the linked list".center(100," "), end="\n\n")
dll.insertAtEnd(50)
dll.print_linked_list()

print("Inserting 20 at the start of the linked list".center(100," "), end="\n\n")
dll.insertAtStart(20)
dll.print_linked_list()

print("Inserting 35 after 30 in the linked list".center(100," "), end="\n\n")
dll.insertAfterItem(25, 35)
dll.print_linked_list()

print("Inserting 30 after 25 in the linked list".center(100," "), end="\n\n")
dll.insertAfterItem(25, 30)
dll.print_linked_list()

print("Inserting 45 before 50 in the linked list".center(100," "), end="\n\n")
dll.insertBeforeItem(50, 45)
dll.print_linked_list()

print("Inserting 32 before 35 in the linked list".center(100," "), end="\n\n")
dll.insertBeforeItem(35, 32)
dll.print_linked_list()

print("Removing first element from the linked list".center(100," "), end="\n\n")
dll.deleteAtFirst()
dll.print_linked_list()

print("Removing Last element from the linked list".center(100," "), end="\n\n")
dll.deleteAtEnd()
dll.print_linked_list()

print("Removing 32 element from the linked list".center(100," "), end="\n\n")
dll.deleteItem(32)
dll.print_linked_list()

present = dll.search(40)
print("Element present in the linked list :", present)
present = dll.search(70)
print("Element present in the linked list :", present)

length = dll.length()
print('Length of the Linked list :', length)

print('Reversing the linked list'.center(100,'-'))
dll.reverseLinkedList()
dll.print_linked_list()