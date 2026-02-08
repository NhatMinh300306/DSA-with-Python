class Queue:
    def __init__(self, capacity):
        self._capacity = capacity
        self.size = 0
        self.front = 0
        self.rear = -1
        self.array = [None] * capacity

    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self._capacity
    
    def enqueue(self, item):
        if self.isFull() == False:
            self.rear = (self.rear + 1) % self._capacity
            self.array[self.rear] = item
            self.size += 1
        else:
            print(f"Queue is Full!")
            return

    def dequeue(self):
        if self.isEmpty() == False:
            item = self.array[self.front]
            self.front = (self.front + 1) % self._capacity
            self.size -= 1
            return item
        else:
            print(f'Queue is Empty!')
            return

    def peek_front(self):
        if self.isEmpty():
            return None
        
        return self.array[self.front]
    
    def peek_rear(self):
        if self.isEmpty():
            return None
        
        return self.array[self.rear]
    
    def display(self):
        if self.isEmpty():
            print(f"Queue is Empty!")
            return
        
        index = self.front
        for _ in range(self.size):
            print(self.array[index], end=" ")
            index = (index + 1) % self._capacity
        print()

q = Queue(5)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

q.display()

print(q.dequeue()) # 10
print(q.dequeue()) # 20

q.enqueue(4)
q.enqueue(5)

q.display()
    