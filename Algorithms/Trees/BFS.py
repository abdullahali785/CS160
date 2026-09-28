import collections

class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

# Tree Traversal using BFS

# Level by level
def BFS(root):
    if not root:
        return []
    
    queue = collections.deque([root])
    visited = []

    while queue:
        for i in range(len(queue)):
            node = queue.popleft()

            if node:
                print(node.val)
                queue.append(node.left)
                queue.append(node.right)
                visited.append(node)

    return visited


# Node by node
def BFS(root):
    if not root:
        return []
    
    queue = collections.deque([root])
    visited = []

    while queue:
        node = queue.popleft()

        if node:
            print(node.val)
            queue.append(node.left)
            queue.append(node.right)
            visited.append(node)

    return visited
