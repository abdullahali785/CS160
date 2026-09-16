class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, key):
        self.heap.append(key)
        self.bubble_up(len(self.heap) - 1) 

    def bubbleUp(self, i): #i is the index of the newly added element. 
        p = (i-1) // 2
        while i > 0 and self.heap[i] < self.heap[p]:
            self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
            i = p
            p = (i-1) // 2
    
    def bubbleDown(self, i): #i is the index of the element that needs to be moved down.
        left = (i * 2) + 1
        right = (i * 2) + 2

        smallest = i

        if left < len(self.heap) and self.heap[smallest] > self.heap[left]:
            smallest = left
        if right < len(self.heap) and self.heap[smallest] > self.heap[right]:
            smallest = right 

        if smallest != i:
            self.heap[smallest], self.heap[i] = self.heap[i], self.heap[smallest]
            self.bubble_down(smallest) 

    def getMin(self):
        if len(self.heap) == 0:
            return None
        
        min = self.heap[0]
        if len(self.heap) > 1:
            self.heap[0] = self.heap.pop()
            self.bubble_down(0)
        else:
            self.heap.pop()
        return min
    
    
class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, key):
        self.heap.append(key)
        self.bubble_up(len(self.heap) - 1)

    def bubbleUp(self, i): #i is the index of the element which is added. 
        p = (i - 1) // 2
        while self.heap[i] > self.heap[p]:
            self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
            i = p
            p = (i - 1) // 2

    def bubbleDown(self, i): #i is the index of the element which is to be moved down. 
        length = len(self.heap)
        left = (i * 2) + 1
        right = (i * 2) + 2

        largest = i

        if left < length and self.heap[largest] < self.heap[left]:
            largest = left
        if right < length and self.heap[largest] < self.heap[right]:
            largest = right

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.bubble_down(largest)

    def getMax(self):
        if len(self.heap) == 0:
            return None
        
        max_val = self.heap[0]
        if len(self.heap) > 1:
            self.heap[0] = self.heap.pop()
            self.bubble_down(0)
        else:
            self.heap.pop()

        return max_val 