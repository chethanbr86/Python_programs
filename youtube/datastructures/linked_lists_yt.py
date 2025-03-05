#https://www.youtube.com/watch?v=1iz9SRWdpX8
class Node:

    def __init__(self, value):
        self.value = value #every node needs to be initilized with a value and reference to another node
        self.next = None #every node when we create it, is not going to have a next node (and that's why None)

class LinkedList: #LinkedList is another class which utilizes the Node class

    def __init__(self): #head node
        self.head = None

    def __repr__(self):
        pass

    #O(n) 
    def __contains__(self): #checks if a value exists in the list
        pass

    def __len__(self):
        pass

    #runtime complexity o(n) - linear runtime - going through all the data
    def append(self, value):
        if self.head is None: #setting head to new node if there is nothing in the list
            self.head = Node(value)
        else: #if there is a head already then going to next element
            last = self.head #if there is a head, make last element to be the head
            while last.next: #as long as there is next element
                last = last.next #now last is next element, one after head
            last.next = Node(value) #inserting value there 

    #o(1) - constant time
    def prepend(self, value):
        first_node = Node(value) #first_node is a node with value which is appended before head (and head can be None or contain a value)
        first_node.next = self.head 
        self.head = first_node

    # O(n)
    def insert(self, value, index): #inserting value at a specific index
        if index == 0: #If inserting at empty list
            self.prepend(value) #you can append also but it will have O(n) time complexity
        else: #if the list is empty and if I am trying to insert at an index that is not 0 then the below code will throw error and hence raising exception
            if self.head is None:
                raise ValueError("Index out of bounds")
            else: #if head is not none
                last = self.head #head position is confirmed now (not assigning value here, only confirming head position)

                #Even though last contains head now, we need to iterate till the index position where we need to insert
                for i in range(index-1):
                    if last.next is None:
                        raise ValueError("Index out of bounds")
                    last = last.next #now we got the last node after which we need to insert (25 in drawio)

                #In the below 3 lines, only the nodes are re-assigned as shown in insert.drawio
                new_node = Node(value) #position 30 in insert.drawio
                new_node.next = last.next #position 35 in insert.drawio
                last.next = new_node



    def delete(self, value):
        pass

    def pop(self, index):
        pass

    def get(self, index):
        pass 

    def print(self):
        pass

if __name__ == "main":
    pass
