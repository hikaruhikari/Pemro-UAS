class data:
    def __init__(self):
        self.Total = 0
        self.Belanja = []

    def Tampil(self):
        print("Barang yang tersedia:")
        print("1. Buku Tulis: Rp. 5000","2. Buku Gambar: Rp. 5000","3. Pensil: Rp. 3000","4. Penghapus: Rp. 2000","5. Penggaris: Rp. 3000","6. Pensil Warna: Rp. 20000","7. Spidol: Rp. 5000","8. Penggaris Besi: Rp. 10000","9. Crayon: Rp. 20000","10. Tipex: Rp. 5000", sep='\n')
        print('=' * 30)

    def Pilih(self, A):
        daftar = {
            "1": ("Buku Tulis", 5000),
            "2": ("Buku Gambar", 5000),
            "3": ("Pensil", 3000),
            "4": ("Penghapus", 2000),
            "5": ("Penggaris", 3000),
            "6": ("Pensil Warna", 20000),
            "7": ("Spidol", 5000),
            "8": ("Penggaris Besi", 10000),
            "9": ("Crayon", 20000),
            "10": ("Tipex", 5000)
        }

        if A in daftar:
            barang, harga = daftar[A]
            while True:
                try:
                    ra = int(input("Jumlah: "))
                    break
                except ValueError:
                    print("Jumlah harus berupa angka.")

            jumlah = ra * harga
            print("Harga = ", jumlah)

            self.Total += jumlah
            self.Belanja.append((barang, ra, jumlah))
        else:
            print("Nomor tidak ada")
        
    def struk(self):
        print("\nStruk belanja")
        print("Daftar belanja:")
        print('-' * 40)
        print("{:<20} {:<10} {:<10}".format("Barang", "Jumlah", "Harga"))
        for barang, jumlah, harga in self.Belanja:
            print("{:<20} {:<10} Rp {:<10}".format(barang, jumlah, harga))
        print('-' * 40)
        print("{:<31} Rp {:<10}".format("Total harga:", self.Total))