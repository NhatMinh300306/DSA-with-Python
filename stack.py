class Stack:
    def __init__(self, capacity):
        self._capacity = capacity
        self.lst = []
        self.top = -1

    def isEmpty(self):
        if self.top == -1:
            return True
        return False
    
    def isFull(self):
        if self.top == self._capacity-1:
            return True
        return False
    
    def push(self, item):
        if self.isFull() == False:
            self.lst.append(item)
            self.top += 1
        else:
            print(f"Stack is Full!")

    def pop(self):
        if self.isEmpty() == False:
            self.top -= 1
            return self.lst.pop()
        else:
            print(f"Stack is empty")

    def peek(self):
        if self.isEmpty() == False:
            return self.lst[self.top]
        else:
            print(f"Stack is Empty!")

    def display(self):
        if self.isEmpty() != True:
            for item in self.lst:
                print(item, end=" ")

stack = Stack(5)
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())
print(stack.peek())
stack.display()

        

    
