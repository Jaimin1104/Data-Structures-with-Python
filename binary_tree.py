class Node:
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self):
        self.root = None
    
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
            
binary_tree = BinaryTree()

binary_tree.root = Node(1)
binary_tree.root.left = Node(2)
binary_tree.root.right = Node(3)
binary_tree.root.left.left = Node(4)

preorder = binary_tree.preorder_traversal(binary_tree.root)
if preorder is None:
    print("Tree is empty")
else:
    print("Preorder Traversal : ", preorder)

inorder = binary_tree.inorder_traversal(binary_tree.root)
if inorder is None:
    print("Tree is empty")
else:
    print("Inorder Traversal : ", inorder)

postorder = binary_tree.postorder_traversal(binary_tree.root)
if postorder is None:
    print("Tree is empty")
else:
    print("Postorder Traversal : ", postorder)
    
print("    Printing Binary Tree\t".center(100,'-'))
binary_tree.print_tree(binary_tree.root)
print("-"*102)