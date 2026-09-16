class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None 

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        if self.front is None:
            return True 
        return False 
    
    def enqueue(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.front = self.rear = new_node
            return
        
        self.rear.next = new_node
        self.rear = new_node 

    def dequeue(self):
        if self.is_empty():
            raise IndexError('Queue is empty!')

        temp = self.front
        self.front = temp.next

        if self.front is None:
            self.rear = None

        return temp.data

    def peek(self):
        if self.is_empty():
            raise IndexError('Queue is empty!')

        return self.front.data

    def display(self):
        if self.is_empty():
            print('Queue is empty!') 
            return
        
        current = self.front
        while current:
            print(current.data, end=' -> ')
            current = current.next 
        print('None')
        
# Example usage:
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.display()

print("Dequeue:", queue.dequeue())
queue.display()