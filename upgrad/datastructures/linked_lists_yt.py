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

    def __contains__(self):
        pass

    def __len__(self):
        pass

    #runtime complexity o(n) - linear runtime - going through all the data
    def append(self, value):
        if self.head is None: #setting head to new node if there is nothing in the list
            self.head = Node(value)
        else: #if there is a head already then going to next element
            last = self.head
            while last.next: #as long as there is next element
                last = last.next
            last.next = Node(value) #if last element 

    #o(1) - constant time
    def prepend(self, value):
        first_node = Node(value) #first_node is a node with value before which a value needs to be prepend
        first_node.next = self.head 
        self.head = first_node

    def insert(self, value, index):
        pass

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
