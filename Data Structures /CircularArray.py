class CircularArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.n = 0 #No. of elememts
        self.f = 0 #First object index
        self.l = 0 #Last object index

    def is_empty(self): 
        return self.n == 0
        
    def size(self):
        return self.n
    
    def rank_to_index(self, rank):
        return (self.f + rank) % self.capacity

    def index_to_rank(self, index):
        return (index - self.f + self.capacity) % self.capacity 

    def element_at_rank(self, rank):
        if self.is_empty():
            raise IndexError('Sequence is empty!')
        
        if rank < 0 or rank >= self.n:
            raise IndexError('Ran out of bounds!')

        return self.array[self.rank_to_index(rank)]

    def insert_first(self, element):
        if self.size() == self.capacity - 1:
            raise IndexError('Sequence is full!')

        self.f = (self.capacity + self.f - 1) % self.capacity
        self.array[self.f] = element
        self.n += 1

    def remove_first(self):
        if self.is_empty():
            raise IndexError('Sequence is empty!')
        
        self.f = (self.f + 1) % self.capacity 
        self.n -= 1

    def insert_last(self, element):
        if self.n == self.capacity - 1:
            raise IndexError('Sequence is full!')

        self.array[self.l] = element
        self.l = (self.l + 1) % self.capacity
        self.n += 1 

    def remove_last(self):
        if self.is_empty():
            raise IndexError('Sequence is empty!')

        self.array[self.l - 1] = None
        self.l = (self.l - 1) % self.capacity
        self.n -= 1

    def insert_at_rank(self, rank, element):
        if self.n == self.capacity - 1:
            raise IndexError('Sequence is full!')
        
        if rank < 0 or rank > self.capacity - 1:
            raise IndexError('Ran out of bounds!')

        if rank == 0:
            self.insert_first(element)
        
        elif rank == self.n:
            self.insert_last(element)

        else:
            if rank < self.n // 2:
                #Shift Left
                self.f = (self.capacity + self.f - 1) % self.capacity
                for i in range(0, rank):
                    self.array[self.rank_to_index(i)] = self.array[self.rank_to_index(i + 1)]

            else:
                #Shift Right
                self.l = (self.l + 1) % self.capacity
                for i in range(self.n, rank, -1):
                    self.array[self.rank_to_index(i)] = self.array[self.rank_to_index(i - 1)]
            
        self.array[self.rank_to_index(rank)] = element
        self.n += 1
            
    def remove_at_rank(self, rank):
        if self.is_empty():
            raise IndexError('Sequence is empty!')
        
        if rank < 0 or rank >= self.n:
            raise IndexError('Rank out of bounds!')

        removed = self.array[self.index_to_rank(rank)]
        if rank < self.n // 2:
            #Shift Right (Elements move forward)
            for i in range(rank, 0, -1):
                self.array[self.rank_to_index(i)] = self.array[self.rank_to_index(i - 1)]
            self.f = (self.f + 1) % self.capacity

        else:
            #Shift Left (Elements move backwards)
            for i in range(rank, self.n - 1):
                self.array[self.rank_to_index(i)] = self.array[self.rank_to_index(i + 1)]
            self.l = (self.l - 1 + self.capacity) % self.capacity
        
        self.n -= 1 
        return removed 

    def replace_at_rank(self, rank, element):
        if self.is_empty():
            raise IndexError('Sequence is empty!')

        if rank < 0 or rank >= self.n:
            raise IndexError('Rank out of bounds!')

        index = self.rank_to_index(rank)
        removed = self.array[index]
        self.array[index] = element
        return removed
 
    def replace_elements(self, e1, e2):
        if self.is_empty():
            raise IndexError('Sequence is empty!')

        if e1 == e2:
            raise ValueError('Both elements same. No replace required!') 

        if e1 is None or e2 is None:
            raise ValueError('Both or one of the elements are not valid!')
             
        replaced = False 
        for i in range(self.n):
            index = self.rank_to_index(i)
            if self.array[index] == e1:
                self.array[index] = e2
                replaced = True 

        return replaced
    
    def swap_elements(self, e1, e2):
        if self.n == 0:
            raise IndexError('Sequence is empty!')

        if e1 == e2:
            raise ValueError('Both elements are same!')

        if e1 is None or e2 is None:
            raise ValueError('1 or both elements are None!')
        
        for i in range(self.capacity):
            if self.array[i] == e1:
                index1 = i
            if self.array[i] == e2:
                index2 = i 

        self.array[index1] = e2
        self.array[index2] = e1 
        return True 

    def reverse(self):
        pass
    
    def rotate(self, k):
        if self.n == 0:
            return 
        
        k = k % self.n
        self.f = (self.f - k) % self.capacity
        self.l = (self.l - k) % self.capacity

    def remove(self, element):
        if self.is_empty():
            raise IndexError('Sequence is empty!')

        for i in range(self.n):
            if self.array[self.rank_to_index(i)] == element:
                self.remove_at_rank(i)
                return element
        raise IndexError('Element not found!')

    def display(self):
        print([self.array[(self.f + i) % self.n] for i in range(self.n)])

seq = CircularArray(10)

seq.insert_last(10)
seq.insert_last(20)
seq.insert_last(30)
seq.insert_last(40)
seq.insert_last(50)

seq.display()