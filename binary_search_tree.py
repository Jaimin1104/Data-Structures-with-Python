class Node:
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self, data, node=None):
        if self.root is None:
            self.root = Node(data)
            return
        if node is None:
            node = self.root
        if data < node.key:
            if node.left is None:
                node.left = Node(data)
                return
            else:
                self.insert(data, node.left)
        if data > node.key:
            if node.right is None:
                node.right = Node(data)
                return
            else:
                self.insert(data, node.right)
                
    def get_minValueNode(self, current=None):
        if current is None:
             current = self.root
        while current.left is not None:
            current = current.left
        return current           
    
    def delete(self, val, node):
        if node is None:
            return node
        if val < node.key:
            node.left = self.delete(val, node.left)
        elif val > node.key:
            node.right = self.delete(val, node.right)
        else:
            if node.left is None:
                temp = node.right
                node=None
                return temp
            elif node.right is None:
                temp = node.left
                node=None
                return temp
            temp = self.get_minValueNode(node.right)
            node.key = temp.key
            node.right = self.delete(node.key, node.right)
        return node
        
    def search(self, val, node):
        if self.root is None:
            return None
        if node is None:
            return None
        if val == node.key:
            return node
        if val < node.key:
            find = self.search(val, node.left)
        if val > node.key:
            find = self.search(val, node.right)
        return find
    
    def print_tree(self, root=None, level=0, prefix="Root :"):
        if self.root is None :
            print("Tree is empty")
            return
        else:
            print("\t"*level, prefix, str(root.key))
        if root.left is not None:
            self.print_tree(root.left, level+1, "Left Child :")
        if root.right is not None:
            self.print_tree(root.right, level+1, "Right Child :")
            
    def preorder_traversal(self, root=None, preorder=[]):
        if self.root is None:
            print("Tree is empty")
            return
        else:
            preorder.append(root.key)
        if root.left is not None:
            self.preorder_traversal(root.left, preorder)
        if root.right is not None:
            self.preorder_traversal(root.right, preorder)
        return preorder

    def inorder_traversal(self, root=None, inorder=[]):
        if self.root is None :
            print("Tree is empty")
            return
        if root.left is not None:
            self.inorder_traversal(root.left, inorder)
        inorder.append(root.key)
        if root.right is not None:
            self.inorder_traversal(root.right, inorder)
        return inorder
    
    def postorder_traversal(self, root=None, postorder=[]):
        if self.root is None :
            print("Tree is empty")
            return
        if root.left is not None:
            self.postorder_traversal(root.left, postorder)
        if root.right is not None:
            self.postorder_traversal(root.right, postorder)
        postorder.append(root.key)
        return postorder
            
bst = BinarySearchTree()

bst.insert(50)
bst.insert(20)
bst.insert(80)
bst.insert(30)
bst.insert(60)
bst.insert(35)
bst.insert(55)
bst.insert(65)
bst.insert(90)
bst.insert(10)

print("    Printing Binary Search Tree    ".center(120,'-'))
bst.print_tree(bst.root)
print("-"*120, end="\n")

preorder = bst.preorder_traversal(bst.root)
if preorder is None:
    print("Tree is empty")
else:
    print("Preorder Traversal : ", preorder)

inorder = bst.inorder_traversal(bst.root)
if inorder is None:
    print("Tree is empty")
else:
    print("Inorder Traversal : ", inorder)

postorder = bst.postorder_traversal(bst.root)
if postorder is None:
    print("Tree is empty")
else:
    print("Postorder Traversal : ", postorder)
    
print("    Printing Binary Search Tree    ".center(120,'-'))
bst.print_tree(bst.root)
print("-"*120, end="\n")

search_value = 30
node = bst.search(search_value, bst.root)
print("    Searching in Binary Search Tree".center(120,'-'))
if node is not None:
    print(search_value, "is present in the binary search tree.")
else:
    print(search_value, "is not present in the binary search tree.")
print("-"*120, end="\n")

print(f" Deleting {search_value} in Binary Search Tree ".center(120,'-'))
ans = bst.delete(search_value, bst.root)
print("    Printing Binary Search Tree    ".center(120,'-'))
bst.print_tree(bst.root)
print("-"*120, end="\n")

search_value = 70
node = bst.search(search_value, bst.root)
print("    Searching in Binary Search Tree".center(120,'-'))
if node is not None and node.key == search_value:
    print(search_value, "is present in the binary search tree.")
else:
    print(search_value, "is not present in the binary search tree.")
print("-"*120, end="\n")

print(f" Deleting {search_value} in Binary Search Tree ".center(120,'-'))
ans = bst.delete(search_value, bst.root)
print("    Printing Binary Search Tree    ".center(120,'-'))
bst.print_tree(bst.root)
print("-"*120, end="\n")