# Linked List
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
class SingleLinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtStart(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def insertAfterItem(self, val, data):
        node = self.head
        new_node = Node(data)
        present = self.search(val)
        if not present:
            print(val, "element is not present in the linked list which you are trying to add element after it.")
            return
        while(node != None):
            node_copy = node
            if node.data == val:
                new_node.next = node.next
                node.next = new_node
            node = node.next
            
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head.next == None:
            self.head.next = new_node
            return
        node = self.head
        while(node.next != None):
            node = node.next
        node.next = new_node
            
    def deleteAtFirst(self):
        print("Deleted item :", self.head.data)
        self.head = self.head.next

    def deleteAtEnd(self):
        node = self.head
        previous_node = None
        while(node.next != None):
            previous_node = node
            node = node.next
        print("Deleted item :", previous_node.next.data)
        previous_node.next = None
    
    def deleteItem(self, val):
        node = self.head
        previous_node = None
        present = self.search(val)
        if not present:
            print(val, "element is not present in the linked list which you are trying to remove")
            return
        if self.head.data == val:
            print("Deleted item :", self.head.data)
            self.head = self.head.next
            return
        while(node != None):
            if node.data == val:
                print("Deleted item :", node.data)
                if node.next != None:
                    previous_node.next = node.next
                else:
                    previous_node.next = None
            previous_node = node
            node = node.next
            
            
    def print_linked_list(self):
        if self.head is None:
            return
        print("Printing Linked List".center(100,"*"))
        node = self.head
        while(node != None):
            print(node.data, end="\t")
            node = node.next
        print()
        
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
        while(current_node != None):
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        self.head = previous_node
            
sll = SingleLinkedList()

print('Adding Head element in the linked list'.center(100,'-'))
sll.head = Node(20)
sll.print_linked_list()

print('Adding 35 & 40 at the end of the linked list'.center(100,'-'))
sll.insertAtEnd(35)
sll.insertAtEnd(40)
sll.print_linked_list()

print('Adding 10 at the start of the linked list'.center(100,'-'))
sll.insertAtStart(10)
sll.print_linked_list()

print('Adding 30 after 20 in the linked list'.center(100,'-'))
sll.insertAfterItem(20,30)
sll.print_linked_list()

print('Adding 25 after 20 in the linked list'.center(100,'-'))
sll.insertAfterItem(20,25)
sll.print_linked_list()

print('Adding 60 after 15 in the linked list'.center(100,'-'))
sll.insertAfterItem(15,60)
sll.print_linked_list()

print('Removing Head element in the linked list'.center(100,'-'))
sll.deleteAtFirst()
sll.print_linked_list()

print('Removing last element in the linked list'.center(100,'-'))
sll.deleteAtEnd()
sll.print_linked_list()

print('Removing 25 element from the linked list'.center(100,'-'))
sll.deleteItem(25)
sll.print_linked_list()

print('Removing 70s element from the linked list'.center(100,'-'))
sll.deleteItem(70)
sll.print_linked_list()

present = sll.search(20)
print("Element present in the linked list :", present)
present = sll.search(50)
print("Element present in the linked list :", present)

length = sll.length()
print('Length of the Linked list :', length)

print('Reversing the linked list'.center(100,'-'))
sll.reverseLinkedList()
sll.print_linked_list()