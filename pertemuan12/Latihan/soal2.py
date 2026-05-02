class Node:
    def __init__(self, data): 
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        #langkah 1
        new = Node(data)

        #langkah 2
        if self.root == None:
            self.root = new
            return
        
        #jika tidak
        #langkah 3
        p = self.root
        q = self.root

        #langkah 4
        while q != None and new.data != p.data:
            #langkah 5
            p = q

            #langkah 6
            if new.data < p.data:
                q = p.left
            else:
                q = p.right

        #langkah 7
        if new.data == p.data:
            print("Woii data nya duplikat!!")
            return
        
        #jika tidak
        #langkah 8
        if new.data < p.data:
            #jika iya
            p.left = new
        #jika tidak
        else:
            p.right = new
        #selesai

bst = BinarySearchTree()

bst.insert(8)
bst.insert(14)
bst.insert(10)
bst.insert(21)
bst.insert(61)

def in_order(node):
    if node is not None:
        in_order(node.left)
        print(node.data, end = " ")
        in_order(node.right)

in_order(bst.root)