class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Binary_Tree:
    def __init__(self):
        self.root=None

    def insert_elements(self):
        data=int(input("Enter the root node : "))
        self.root=Node(data)
        self.get_other_nodes(self.root)

    def get_other_nodes(self,node):
        left = input(f"Add left child to the node {node.data}? (y/n): ").lower() == 'y'
        if left:
            data=int(input("Enter the number you want insert : "))
            node.left=Node(data)
            self.get_other_nodes(node.left)
        right = input(f"Add right child to the node {node.data}? (y/n): ").lower() == 'y'
        if right:
            data=int(input("Enter the number you want insert x : "))
            node.right=Node(data)
            self.get_other_nodes(node.right)
    
    def display(self,node):
        if not node:
            return 
        print(node.data)
        self.display(node.left)
        self.display(node.right)

    def pretty_display(self,node,level):
        if not node:
            return
        self.pretty_display(node.right,level+1)
        if level != 0:
            for i in range(level-1):
                print("|  ")
            print("|------>",node.data)
        else:
            print(node.data)
        self.pretty_display(node.left,level+1)
        
if __name__=="__main__":
    tree=Binary_Tree()
    tree.insert_elements()
    tree.pretty_display(tree.root,0)