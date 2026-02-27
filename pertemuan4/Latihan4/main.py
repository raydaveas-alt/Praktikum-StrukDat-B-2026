from kurs import kurs
from tabulate import tabulate
from konverter import idr_asing, asing_idr

print("=== KONVERTER MATA UANG ===")

tabel = []
for kode, nilai in kurs.items():
    tabel.append([kode, f"{nilai:,}".replace(",", ".")])

print(tabulate(tabel, headers=["Kode", "Kurs"], tablefmt="grid"))

# input
dari = input("\nDari (IDR/USD/EUR/SGD/JPY): ")
ke = input("Ke (IDR/USD/EUR/SGD/JPY): ")
jumlah = float(input("Jumlah: "))

# proses
if dari == "IDR":
    hasil = idr_asing(jumlah, ke)
    print(f"\nRp {jumlah:,.0f}".replace(",", ".") + f" = {hasil:.2f} {ke}")
elif ke == "IDR":
    hasil = asing_idr(jumlah, dari)
    print(f"\n{jumlah:.2f} {dari} = Rp {hasil:,.0f}".replace(",", "."))
else:
    idr = asing_idr(jumlah, dari)
    hasil = idr_asing(idr, ke)
    print(f"\n{jumlah:.2f} {dari} = {hasil:.2f} {ke}")