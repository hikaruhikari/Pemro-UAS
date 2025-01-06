from inputan import view as V
class process:
    def __init__(self):
        self.piu = V()

    def run(self):
        while True:
            print("Selamat Datang")
            sip = input("Ingin masuk? (yes/no): ").lower()
            if sip == "yes":
                self.piu.Tampil()
                self.piu.Pilih()
                self.piu.Struk()
            else:
                print("Terima Kasih")
                break

if __name__ == '__main__':
    process().run()
