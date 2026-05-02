class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_root(self, data):
        node = Node(data)
        self.root = node

tree = BinaryTree()

tree.insert_root(2)
print(tree.root.data)

BinaryTree.insert(1)