from pendataan import data
class view:
    def __init__(self):
        self.dta = data()

    def Tampil(self):
        Masuk = input("Tampilkan barang? (yes/no): ").lower()
        if Masuk == "yes":
            self.dta.Tampil()
        else:
            print("Oke")
            

    def Pilih(self):
        while True:
            A = input("Pilih barang (dengan angka): ")
            if not A.isdigit() or int(A) not in range(1, 11):
                print("Nomor tidak benar")
                continue

            self.dta.Pilih(A)
            saus = input("Mau beli barang lagi? (yes/no): ").lower()
            if saus != "yes":
                break

    def Struk(self):
        bang = input("Mau lihat struk belanja? (yes/no): ").lower()
        if bang == "yes":
            self.dta.struk()
            print("Terima kasih")
        else:
            print("Terima kasih")

    

    
