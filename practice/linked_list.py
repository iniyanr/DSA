class Node:
    def __init__(self,data:int):
        self.num=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    def insert_element(self,data):
        self.size+=1
        if self.head == None:
            new_node=Node(data)
            self.head,self.tail=new_node,new_node
            return
        new_node=Node(data)
        self.tail.next=new_node
        self.tail=new_node

    def insert_element_at_first(self,data):
        self.size+=1
        if self.head == None:
            new_node=Node(data)
            self.head,self.tail=new_node,new_node
            return
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    
    def insert_at_position(self,data,index):
        if self.head==None and index != 0:
            return "List Empty"
        if index==0:
            self.insert_element_at_first(data)
            return
        if self.size < index:
            print(f"Size of list : {self.size}") 
            return    
        count=0
        new_node=Node(data)
        tmp=self.head
        while tmp != None:
            if count == (index-1):
                new_node.next=tmp.next
                tmp.next=new_node
                self.size+=1
                return
            tmp=tmp.next
            count+=1
        
    def delete_node(self,index):   
        if self.head == None:
            return      
        if self.size <= index or index<0:
            print(f"Length of linked list : {self.size}")     
            return 
        if index == 0:
            self.head=self.head.next
            if self.head == None:
                self.tail=None
            self.size-=1
            return 
        
        count=0
        tmp=self.head
        while tmp is not None:
            if count == index-1 and tmp.next is not None:
                tmp.next=tmp.next.next
                if tmp.next == None:
                    self.tail=tmp
                self.size-=1
                return 
            tmp=tmp.next
            count+=1
    
    def print_linked_list(self):
        tmp=self.head
        while tmp is not None:
            print(tmp.num,end="->")
            tmp=tmp.next
        print("END")
        print(f"\nSize of list : {self.size}")
        
    def reverse_linked_list(self):
        prev_node=None
        current_node=self.head
        self.tail=self.head
        while current_node is not None:
            next_node=current_node.next
            current_node.next=prev_node
            prev_node=current_node
            current_node=next_node
        self.head=prev_node
    
    def insert_using_recursion(self,data,index,count,node=None):
        if index==0:
            node=Node(data)
            self.head=node
            return
            
        if node is None:
           node=self.head
        if node is None:
            print("ll empty")
            return
        if count==index-1:
            new_node=Node(data)
            new_node.next=node.next
            node.next=new_node
            if node.next==None:
                self.tail=new_node
            return
        self.insert_using_recursion(data,index,count+1,node.next)




first=LinkedList()
for i in range(0,11):
    first.insert_using_recursion(i+1,i,0,first.head)
print("linked list : ",end="->")
first.print_linked_list()


