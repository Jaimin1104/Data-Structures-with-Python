class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
class CircularLinkedList:
    def __init__(self):
        self.head = None
        
    def insertAtStart(self, data):
        new_node = Node(data)
        new_node.next = self.head
        node = self.head
        while(node.next != self.head):
            node = node.next
        node.next = new_node
        self.head = new_node
        
    def insertAfterItem(self, val, data):
        present = self.search(val)
        if not present:
            print(val, "element is not present in the linked list which you are trying to add element after it.")
            return
        new_node = Node(data)
        node = self.head
        while(node.next != self.head):
            if node.data == val:
                break
            node = node.next
        new_node.next = node.next
        node.next = new_node
        
    def insertAtEnd(self, data):
        new_node = Node(data)
        new_node.next = self.head
        node = self.head
        if self.head is None:
            self.head = Node(data)
            self.head.next = self.head
            return
        while(node.next != self.head):
            node = node.next
        node.next = new_node
        
    def deleteAtFirst(self):
        if self.head is None:
            return
        node = self.head
        print("Deleted item :", self.head.data)
        while(node.next != self.head):
            node = node.next
        self.head = self.head.next
        node.next = self.head
        
    def deleteAtEnd(self):
        node = self.head
        previous_node = None
        while(node.next != self.head):
            previous_node = node
            node = node.next
        print("Deleted item :", node.data)
        previous_node.next = self.head
        
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
            if(node.data == val):
                previous_node.next = node.next
                print("Deleted item :", node.data)
                return
            previous_node = node
            node = node.next
        print("Deleted item :", node.data)
        previous_node.next = self.head
            
    def print_linked_list(self):
        if self.head is None:
            return
        print("Printing Linked List".center(100,"*"))
        node = self.head
        while(node.next != self.head):
            print(node.data, end="\t")
            node = node.next
        print(node.data, end="\n")
        
    def search(self, val):
        if self.head is None:
            return false
        node = self.head
        found = False
        while(node.next != self.head):
            if node.data == val:
                # found = True
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
        if self.head is None:
            return
        previous_node = None
        current_node = self.head
        next_node = self.head.next
        while (next_node != self.head):
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
            next_node = next_node.next
        current_node.next = previous_node
        self.head = current_node
        node = self.head
        while(node.next != None):
            node = node.next
        node.next = self.head
        
cll = CircularLinkedList()

print('Adding 20 and 30 element in the linked list'.center(100,'-'))
cll.insertAtEnd(20)
cll.insertAtEnd(30)
cll.insertAtEnd(50)
cll.print_linked_list()

print('Adding 10 element at the start in the linked list'.center(100,'-'))
cll.insertAtStart(10)
cll.print_linked_list()

print('Adding 15 element after 10 element in the linked list'.center(100,'-'))
cll.insertAfterItem(10,15)
cll.print_linked_list()

print('Adding 25 element after 20 element in the linked list'.center(100,'-'))
cll.insertAfterItem(20,25)
cll.print_linked_list()

print('Adding 40 element after 30 element in the linked list'.center(100,'-'))
cll.insertAfterItem(30,40)
cll.print_linked_list()

print('Adding 35 element after 30 element in the linked list'.center(100,'-'))
cll.insertAfterItem(30,35)
cll.print_linked_list()

print('Removing Head element in the linked list'.center(100,'-'))
cll.deleteAtFirst()
cll.print_linked_list()

print('Removing last element in the linked list'.center(100,'-'))
cll.deleteAtEnd()
cll.print_linked_list()

print('Removing 20 element from the linked list'.center(100,'-'))
cll.deleteItem(20)
cll.print_linked_list()

print('Removing 70s element from the linked list'.center(100,'-'))
cll.deleteItem(70)
cll.print_linked_list()

present = cll.search(15)
print("Element present in the linked list :", present)
present = cll.search(50)
print("Element present in the linked list :", present)

length = cll.length()
print('Length of the Linked list :', length)

print('Reversing the linked list'.center(100,'-'))
cll.reverseLinkedList()
cll.print_linked_list()