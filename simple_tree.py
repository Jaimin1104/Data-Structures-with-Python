class Node:
    def __init__(self, data=None):
        self.key = data
        self.children = []
        
class Tree:
    def __init__(self):
        self.root = None
    
    def add_child(self, key, data, node=None):
        if node is None:
            node = self.root
        if key == node.key:
            node.children.append(Node(data))
            return
        for child in node.children:
            self.add_child(key, data, child)
            
    def delete_node(self, key, root):
        if root is None:
            return None
        if root.key == key:
            return None
        new_children = []
        for child in root.children:
            new_child = self.delete_node(key, child)
            if new_child is not None:
                new_children.append(new_child)
        root.children = new_children
        return root
            
    def print_tree(self, root=None, level=0, prefix="Root :"):
        if root is not None:
            print("\t"*level, prefix, str(root.key))
            for child in root.children:
                self.print_tree(child, level+1, "Child :")
                
    def heightOfTree(self, root=None):
        level = 0
        if root is not None:
            for child in root.children:
                level = max(level, self.heightOfTree(child))
        return level+1
                
    def search_node(self, root=None, val=None):
        present = False
        if root is not None:
            if root.key == val:
                present = True
            for child in root.children:
                self.search_node(child, val)
        if present:
            print(val, "is present in the tree")
        else:
            print(val, "is not present in the tree")
                
        
tree = Tree()

print("Adding nodes in the tree".center(100," "))
tree.root = Node(500)
tree.add_child(500, 530)
tree.add_child(500, 550)
tree.add_child(500, 560)
tree.add_child(530, 535)
tree.add_child(530, 537)
tree.add_child(535, 535.3)
tree.add_child(535.3, 535.35)
tree.add_child(535, 535.6)
tree.add_child(550, 555)

print("-"*100)
tree.print_tree(tree.root)
print("-"*100)

print("After deleting 550 from the tree".center(100," "))
tree.delete_node(550, tree.root)

print("-"*100)
tree.print_tree(tree.root)
print("-"*100)

height = tree.heightOfTree(tree.root)
print("Height of the Tree : ", height)