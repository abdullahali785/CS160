class Node:
    def __init__(self, key):
        self.value = key 
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, current, key):
        if key > current.value:
            if current.right:
                self._insert(current.right, key)
            else:
                current.right = Node(key)

        else:
            if current.left:
                self._insert(current.left, key)
            else:
                current.left = Node(key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, current, key):
        while current:
            if current.value == key:
                return True
            elif current.value > key:
                self._search(current.left, key)
            else:
                self._search(current.right, key)
        return False 

    def find_min(self):
        current = self.root
        while current.left:
            current = current.left
        return current.value 

    def find_max(self):
        current = self.root
        while current.right:
            current = current.right
        return current.value

    def find_min_node(self, node):
        current = node 
        while current.left:
            current = current.left
        return current  
    

class ArrayBinaryTree:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.tree = [None] * capacity
        self.size = 0 

    def insert(self, key):
        if self.size < self.capacity:
            self.tree[self.size] = key
            self.size += 1
        else:
            raise IndexError('Tree is full!')

    def left_child_index(self, i):
        left = (i * 2) + 1 
        if left > self.size:
            return None
        return left

    def right_child_index(self, i):
        right = (i * 2) + 2
        if right > self.size:
            return None
        return right

    def inorder(self, i=0, result=None):
        if result is None:
            result = []
        if i >= self.size or self.tree[i] is None:
            return
        
        left = self.left_child_index(i)
        if left:
            self.inorder(left, result)

        result.append(self.tree[i])

        right = self.right_child_index(i)
        if right:
            self.inorder(right, result)

        return result     

    def preorder(self, i=0, result=None):
        if result == None:
            result = []
        if i >= self.size or self.tree[i] is None:
            return
        
        result.append(self.tree[i])

        left = self.left_child_index(i)
        if left:
            self.preorder(left, result)

        right = self.right_child_index(i)
        if right:
            self.preorder(right, result)

        return result

    def postorder(self, i=0, result=None):
        if result is None:
            result = []
        if i >= self.size or self.tree[i] is None:
            return
        
        left = self.left_child_index(i)
        if left:
            self.postorder(left, result)

        right = self.right_child_index(i)
        if right:
            self.postorder(right, result)

        result.append(self.tree[i])
        return result

    def search(self, key):
        for i in range(self.size):
            if self.tree[i] == key:
                return i
        return False 


# bt = BinaryTree()
# bt.insert(10)
# bt.insert(5)
# bt.insert(20)
# bt.insert(3)
# bt.insert(7)
# bt.insert(15)
# bt.insert(25)

# print("In-order traversal:", bt.inorder())
# print("Pre-order traversal:", bt.preorder())
# print("Post-order traversal:", bt.postorder())

# print("Search for 7:", bt.search(7))
# print("Search for 30:", bt.search(30))

# print("Minimum value in the tree:", bt.find_min())
# print("Maximum value in the tree:", bt.find_max())


# bt = ArrayBinaryTree(15)

# bt.insert(10)
# bt.insert(5)
# bt.insert(20)
# bt.insert(3)
# bt.insert(7)
# bt.insert(15)
# bt.insert(25)

# print("In-order traversal:", bt.inorder())
# print("Pre-order traversal:", bt.preorder())
# print("Post-order traversal:", bt.postorder())

# print("Search for 7:", bt.search(7))
# print("Search for 30:", bt.search(30))