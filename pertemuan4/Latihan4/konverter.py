from kurs import kurs

def idr_asing(jumlah, kode):
    return jumlah / kurs[kode]

def asing_idr(jumlah, kode):
    return jumlah * kurs[kode]