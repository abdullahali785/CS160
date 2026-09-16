class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.top = None
        self._size = 0 

    def is_empty(self):
        if self.top is None:
            return True
        return False

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node 
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty!")
        item = self.top.data
        self.top = self.top.next
        self._size -= 1
        return item 

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty!")
        return self.top.data 

    def size(self):
        return self._size

    def __str__(self):
        result = []
        current = self.top
        while current:
            result.append(current.data)
            current = current.next
        return str(result)
    
class ArrayStack:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.top = -1 
        self.stack = [None] * capacity 

    def is_empty(self):
        if self.top == -1:
            return True
        return False
        #You can also write return self.top == -1. The boolean of the given statement is returned in this case. 

    def is_full(self):
        if self.top == self.capacity - 1:
            return True 
        return False
        # You can also write return self.top == self.capacity - 1. The boolean of the given statement is returned in this case. 

    def push(self, item):
        if stack.is_full():
            raise OverflowError("Stack is full!")
        self.top += 1
        self.stack[self.top] = item 

    def pop(self):
        if stack.is_empty():
            raise IndexError("Stack is empty!")
        item = self.stack[self.top]
        self.stack[self.top] = None #This is optional.
        self.top -= 1
        return item

    def peek(self):
        if stack.is_empty():
            raise IndexError('Stack is empty!')
        return stack[self.top]

    def size(self):
        return self.top + 1

    def __str__(self):
        return str([self.stack[i] for i in range (self.top + 1)])


if __name__ == "__main__":
    stack = ArrayStack(5)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack)
    stack.push(4)
    print(stack)
    print('Popped:', stack.pop())
    print(stack)
    print(stack.size)
