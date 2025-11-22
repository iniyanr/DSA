class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        self.height=0

class BST:
    def __init__(self):
        self.root=None

    def get_height(self,node):
        if not node:
            return -1
        return node.height
    
    def isEmpty(self):
        return self.root == None
    
    def insert_root(self,val):
        self.root = self.insert(val, self.root)
        
    def insert(self,val,node):
        if node is None:
            return Node(val)

        if val < node.val:
            node.left = self.insert(val, node.left)
        else:
            node.right = self.insert(val, node.right)
        
        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
        return node
    def is_balanced(self, node="__root__"):
        if node == "__root__":
            node = self.root
            if node is None:
                return True

        # Base case for recursion
        if node is None:
            return True

        lh = self.get_height(node.left)
        rh = self.get_height(node.right)

        if abs(lh - rh) > 1:
            return False

        return self.is_balanced(node.left) and self.is_balanced(node.right)

    
    def display(self, node=None, indent=""):
        if node is None:
            node = self.root
            if node is None:
                print("Tree is empty")
                return

        print(indent + str(node.val))

        if node.left:
            self.display(node.left, indent + "L--> ")

        if node.right:
            self.display(node.right, indent + "R--> ")

b = BST()

b.insert_root(10)
b.insert_root(5)
b.insert_root(15)
b.insert_root(2)
b.insert_root(7)

b.display()
print("Tree is balanced :", b.is_balanced())
