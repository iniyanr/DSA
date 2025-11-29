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

    def preorder(self,node):
        if node is None:
            return
        print(node.val,end="->")
        self.preorder(node.left)
        self.preorder(node.right)

    def inorder(self,node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.val,end="->")
        self.inorder(node.right)
    
    def postorder(self,node):
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.val,end="->")
    
    
b = BST()

b.insert_root(10)
b.insert_root(5)
b.insert_root(15)
b.insert_root(2)
b.insert_root(7)

print("Preorder :",end=" ")
b.preorder(b.root)
print()
print("Inorder : ",end=" ")
b.inorder(b.root)
print()
print("Postorder : ",end=" ")
b.postorder(b.root)
print()
print("Tree is balanced :", b.is_balanced())
