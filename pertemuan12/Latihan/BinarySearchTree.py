class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,data):
        #Langkah 1
        new = Node(data)

        #Langkah 2
        if self.root is None:
            #Jika iya
            self.root = new
            return
        
        #Jika tidak
        #Langkah 3
        P = self.root
        Q = self.root

        #Langkah 4
        while Q != None and new.data != P.data:
            #Langkah 5
            P = Q
            #Langkah 6
            if new.data < P.data:
                #Jika iya
                Q = P.left
            else:
                #Jika tidak
                Q = P.right

            #Langkah 7
        if new.data == P.data:
            #Jika iya
            print("Datanya duplikat")
            return

        #Jika tidak
        #Langkah 8
        if new.data < P.data:
            #Jika iya
            P.left = new
        else:
            #Jika tidak
            P.right = new

bst = BinarySearchTree()

bst.insert(56)
bst.insert(67)
bst.insert(3)
bst.insert(49)
bst.insert(25)

def inOrder(node):
    if node is not None:
        inOrder(node.left)
        print(node.data,end=" ")
        inOrder(node.right)

inOrder(bst.root)