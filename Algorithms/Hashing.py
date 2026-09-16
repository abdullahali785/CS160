class ChainingHashTable:
    def __init__(self, size=10):
        self.size = 10
        self.table = [SinglyLinkedList() for _ in range(self.size)]

    def hash(self, key):
        return (key % self.size)
    
    def insert(self, key, value):
        index = self.hash(key)
        self.table[index].insert(key, value)

    def search(self, key):
        index = self.hash(key)
        return self.table[index].search(key)
    
    def remove(self, key):
        index = self.hash(key)
        self.table[index].remove(key)

    def display(self):
        res = ""
        for i, bucket in enumerate(self.table):
            res += f"bucket {i}: {bucket.display()}\n"
        return res

class DoubleHashing:
    def __init__(self, size=10):
        self.size = 10
        self.table = [None] * size 

    def hash_1(self, key):
        return key % self.size 
    
    def hash_2(self, key):
        q = 3
        return q - (key % q)

    def insert(self, key, value):
        i = self.hash_1(key)
        j = 0
        added = False 

        while not added and j < self.size:
            index = ( (i + (j * self.hash_2(key)) ) % self.size )

            if self.table[index] == None:
                self.table[index] = value
                added = True 
            else:
                j = j+1 

        if not added:
            print('Hash Table is full!')

    def search(self, key):
        i = self.hash_1(key)
        j = 0

        while j < self.size:
            index = ( (i + (j * self.hash_2(key)) ) % self.size ) 
            elem = self.table[index]

            if elem == None:
                print('No such key present inside Hash Table!')
                return False 
            elif index == self.hash_1(key):
                print(f"{elem}")
                return True
            else: 
                j = j+1 

        print('No such key found!')
        return False 

    def display(self):
        res = ""
        for i, bucket in enumerate(self.table):
            res += f"bucket {i}: {bucket}\n"
        return res


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        
    def insert(self, key, value):
        current = self.head
        while current:
            if current.key == key:
                current.value = value
                return 
            current = current.next
        
        new = Node(key, value)
        new.next = self.head
        self.head = new

    def search(self, key):
        current = self.head
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None
    
    def remove(self, key):
        current = self.head
        prev = None

        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next 
                else:
                    self.head = current.next
                return True
            prev = current 
            current = current.next
        return False 
    
    def display(self):
        res = []
        current = self.head
        while current:
            res.append(f"{current.key}: {current.value}")
            current = current.next
        return " -> ".join(res) if res else "Empty"


h = DoubleHashing()
h.insert(5, 'Apple')
h.insert(7, 'Dog')
h.insert(9, 'Pal')
h.insert(15, 'Cat')
h.insert(1, 'Yes')
print(h.display())

h.search(0)