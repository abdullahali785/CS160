import collections

class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

# Tree Traversal using BFS
def BFS(root):
    visited = []
    queue = collections.deque()
    queue.appendleft(root)

    while queue:
        queueLenght = len(queue)
        for i in range(queueLenght):
            node = queue.pop()

            if node:
                queue.appendleft(node.left)
                queue.appendleft(node.right)
                visited.append(node)

    return visited 