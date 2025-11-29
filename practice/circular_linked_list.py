class Node:
    def __init__(self,data:int):
        self.num=data
        self.next=None

class CircularLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    def insert_element_at_end(self,data):
        self.size+=1
        if self.head == None:
            new_node=Node(data)
            self.head,self.tail=new_node,new_node
            self.tail.next=self.head
            return
        new_node=Node(data)
        new_node.next=self.head
        self.tail.next=new_node
        self.tail=new_node

    def insert_element_at_first(self,data):
        self.size+=1
        if self.head == None:
            new_node=Node(data)
            self.head,self.tail=new_node,new_node
            self.tail.next=self.head
            return
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
        self.tail.next=self.head
    
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
        while True:
            if count == (index-1):
                new_node.next=tmp.next
                tmp.next=new_node
                self.size+=1
                if new_node.next is self.head:
                    self.tail=new_node
                    self.tail.next=self.head   
                return
            tmp=tmp.next
            if tmp == self.head:
                break
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
            else:
                self.tail.next=self.head
            self.size-=1
            return 
        
        count=0
        tmp=self.head
        while True:
            if count == index - 1:
                node_to_delete = tmp.next
                tmp.next = node_to_delete.next
                if node_to_delete == self.tail:
                    self.tail = tmp
                self.tail.next = self.head
                self.size -= 1
                return
            tmp = tmp.next
            count += 1
            if tmp == self.head:
                break
    
    def print_linked_list(self):
        tmp=self.head
        while True:
            print(tmp.num,end="->")
            tmp=tmp.next
            if self.head==tmp:
                break
        print("END")
        print(f"\nSize of list : {self.size}")
        
    
first=CircularLinkedList()

for i in range(1,11):
    first.insert_element_at_end(i)
print("linked list : ",end="->")
first.print_linked_list()


