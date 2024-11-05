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

    def append(self, value):
        pass

    def prepend(self, value):
        pass

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
