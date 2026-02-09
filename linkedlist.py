class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def createNode(self, item):
        return Node(item)
    
    def addFirst(self, item):
        newNode = self.createNode(item)
        if self.head is None:
            self.head = newNode
            self.size += 1
            return
        else:
            newNode.next = self.head
            self.head = newNode
            self.size += 1

    def addLast(self, item):
        newNode = self.createNode(item)
        if self.head is None:
            self.head = newNode
            self.size += 1
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = newNode
        self.size += 1

    def deleteFirst(self):
        if self.head is None:
            return
        self.head = self.head.next
        self.size -= 1
        
    def deleteLast(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            self.size -= 1
            return
        
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None
        self.size -= 1
    
    def display(self):
        if self.head is None:
            return
        else:
            temp = self.head
            while(temp is not None):
                print(temp.item, end=" ")
                temp = temp.next
    
list = LinkedList()
list.addFirst(1)
list.addFirst(2)
list.addLast(3)
list.deleteFirst()
list.deleteLast()
list.display()