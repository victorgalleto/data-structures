from collections import deque

stack = deque()
list = []
#dir(stack) see all the methods
# stack class must be implemented first in script

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)
    
    def pop(self):
        return self.container.pop()

    def is_empty(self):
        return len(self.container)==0

    def size(self):
        return len(self.container)
    

stack.append('https://www.cnn.com/')
stack.append('https://www.cnn.com/1')
stack.appendleft('https://www.cnn.com/2')
print(stack)
print(stack.pop())