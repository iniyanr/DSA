class Node:
    def __init__(self,data:int):
        self.num=data
        self.next=None
        self.prev=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def insert_element_at_last(self,data):
        self.size+=1
        if self.head == None:
            new_node=Node(data)
            self.head,self.tail=new_node,new_node
            return
        new_node=Node(data)
        new_node.prev=self.tail
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
        self.head.prev=new_node
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
                new_node.prev=tmp
                if new_node.next is not None:
                    new_node.next.prev=new_node
                else:
                    self.tail=new_node
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
            if self.head!=None:
                self.head.prev=None
            if self.head == None:
                self.tail=None
            self.size-=1
            return 
        
        count=0
        tmp=self.head
        while tmp is not None:
            if count == index-1 and tmp.next is not None:
                tmp.next=tmp.next.next
                if tmp.next != None:
                    tmp.next.prev=tmp
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
            prev_val=tmp.prev.num if tmp.prev else None
            next_val=tmp.next.num if tmp.next else None
            print(f"Prev : {prev_val} , Data : {tmp.num} , Next : {next_val}")
            tmp=tmp.next
        print("END")
        print(f"\nSize of list : {self.size}")
        

first=DoublyLinkedList()
for i in range(1,11):
    first.insert_element_at_first(i)
first.insert_at_position(23,2)

# first.delete_node(9)

first.delete_node(10)
first.print_linked_list()


