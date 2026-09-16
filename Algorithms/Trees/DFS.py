class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Tree Traversal using DFS
def Inorder(root):
    if root:
        Inorder(root.left)
        print(root.data)
        Inorder(root.right)

def Preorder(root):
    if root:
        print(root.data)
        Preorder(root.left)
        Preorder(root.right)

def Postorder(root):
    if root:
        Postorder(root.left)
        Postorder(root.right)
        print(root.data)

def Iterative(root):
    stack, visited = [], []
    stack.append(root)

    while stack:
        node = stack.pop()

        if node: # Preorder
            print(node.data)
            stack.append(node.right)
            stack.append(node.left)
            visited.append(node)

    return visited 