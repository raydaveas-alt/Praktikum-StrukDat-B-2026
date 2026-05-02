class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_manual(self):
        self.root = Node("A")
        self.root.left = Node("B")
        self.root.right = Node("C")
        self.root.left.left = Node("D")
        self.root.left.right = Node("E")
        self.root.right.left = Node("F")
    
    def traverse_preorder(self, node, preorder):
        if node is not None:
            preorder.append(node.data)
            self.traverse_preorder(node.left, preorder)
            self.traverse_preorder(node.right, preorder)

    def traverse_inorder(self, node, inorder):
        if node is not None:
            self.traverse_inorder(node.left, inorder)
            inorder.append(node.data)
            self.traverse_inorder(node.right, inorder)
    
    def traverse_postorder(self, node, postorder):
        if node is not None:
            self.traverse_postorder(node.left, postorder)
            self.traverse_postorder(node.right, postorder)
            postorder.append(node.data)

    def leaf_nodes(self, node, leaf):
        if node:
            if node.left is None and node.right is None:
                leaf.append(node.data)
            self.leaf_nodes(node.left, leaf)
            self.leaf_nodes(node.right, leaf)

asdf = BinaryTree()
    
print('SISTEM AUDIT DISTRIBUSI "CEPAT SAMPAI"')
print('======================================')
print('[INFO] Membangun struktur Gudang...')
asdf.insert_manual()

print('[INFO] Struktur berhasil dibuat.')
print('\nHasil audit:')

preorder = []
asdf.traverse_preorder(asdf.root, preorder)
print("1. Pre-order:", " - ".join(preorder))

inorder = []
asdf.traverse_inorder(asdf.root, inorder)
print("2. In-order:", " - ".join(inorder))

postorder = []
asdf.traverse_postorder(asdf.root, postorder)
print("3. Post-order:", " - ".join(postorder))

print("")

leaf = []
asdf.leaf_nodes(asdf.root, leaf)
print("[DATA] Gudang Ujung:", " - ".join(leaf))
print('======================================')
print('Audit Selesai!')