import collections

class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

# Tree Traversal using BFS

# Level by level
def BFS(root):
    queue = collections.deque()
    visited = []
    queue.append(root)

    while queue:
        for i in range(len(queue)):
            node = queue.pop()

            if node:
                print(node.val)
                queue.appendleft(node.right)
                queue.appendleft(node.right)
                visited.append(node)

    return visited


# Node by node
def BFS(root):
    queue = collections.deque()
    visited = []
    queue.append(root)

    while queue:
        node = queue.pop()

        if node:
            print(node.val)
            queue.appendleft(node.right)
            queue.appendleft(node.right)
            visited.append(node)

    return visited
