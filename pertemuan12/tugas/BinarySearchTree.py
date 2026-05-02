class Node:
    def __init__(self, id_buku, judul):
        self.data = id_buku
        self.nama = judul
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, id_buku, judul):
        new = Node(id_buku, judul)

        if self.root is None:
            self.root = new
            return
        
        P = self.root
        Q = self.root

        while Q is not None and new.data is not P.data:
            P = Q
            if new.data < P.data:
                Q = P.left
            else:
                Q = P.right
        
        if new.data == P.data:
            print("Datanya duplikat")
            return
        
        if new.data < P.data:
            P.left = new
        else:
            P.right = new
        
        print(f"Berhasil memasukkan: ID {id_buku} - {judul}")
    
    def search(self, id_buku):
        P = self.root

        while P is not None:
            if id_buku == P.data:
                return P
            elif id_buku < P.data:
                P = P.left
            else:
                P = P.right

        return None
    
    def traversal_inorder(self, node, nomor):
        if node is not None:
            nomor = self.traversal_inorder(node.left, nomor)
            print(f'{nomor}. {node.data} - {node.nama}')
            nomor += 1
            nomor = self.traversal_inorder(node.right, nomor)
        return nomor
    
    def get_min(self):
        nilai = self.root
        while nilai.left is not None:
            nilai = nilai.left
        return nilai
    
    def get_max(self):
        nilai = self.root
        while nilai.right is not None:
            nilai = nilai.right
        return nilai
    
    def height(self, node):
        if node is None:
            return -1
        left = self.height(node.left)
        right = self.height(node.right)
        return max(left, right) + 1



BST = BinarySearchTree()

print('SISTEM KATALOGF PERPUSTAKAAN "ILMU TERANG"')
print("=========================================")
print('[INFO] Koleksi Buku (In-order traversal):')

BST.insert(50, "Dasar Pemrograman")
BST.insert(30, "Struktur Data")
BST.insert(70, "Kecerdasan Buatan")
BST.insert(20, "Matematika Diskrit")
BST.insert(40, "Basis Data")
BST.insert(60, "Jaringan Komputer")
BST.insert(80, "Sistem Operasi")
print("")

hasil = BST.search(60)
print(f'[SEARCH] Mencari ID 60...', end=" ")
if hasil:
    print('Ditemukan! Judul:', hasil.nama)
else:
    print ('Data tidak ditemukan.')

hasil = BST.search(100)
print(f'[SEARCH] Mencari ID 100...', end=" ")
if hasil:
    print('Ditemukan! Judul:', hasil.nama)
else:
    print ('Data tidak ditemukan.')

print()
print("[STATISTIK] ID Terkecil:", BST.get_min().data)
print("[STATISTIK] ID Terbesar:", BST.get_max().data)
print('[INFO] Tinggi (Height) Tree:', BST.height(BST.root))

print("=========================================")
print('Simulasi selesai!')