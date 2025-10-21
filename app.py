# ============= OOP =============
class Kendaraan:
    def __init__(self, merk, color):
        self.merk = merk
        self.color = color

    def info(self):
        print(
            f"""\nini adalah {self.merk}
kendaraan ini warna nya {self.color}"""
        )


# ============= Turunan =============
class SuperBike(Kendaraan):
    def __init__(self, merk, color, max_speed):
        super().__init__(merk, color)
        self.max_speed = max_speed

    def BikeInfo(self):
        print("\n# ============= Output =============")

        print(
            f"""\nini adalah superbike merk {self.merk}
warna motor ini adalah {self.color}
kecepatan maximum superbike ini adalah {self.max_speed} km/jam"""
        )


# ============= input =============
print("\n# ============= input kendaraan =============\n")

jenis_kendaraan = input("masukan jenis kendaraan (motor/mobil) : ").lower()

if jenis_kendaraan == "mobil":
    merk = input("masukan merk kendaraan : ")
    color = input("masukan warna kendaraan : ")
    mobil = Kendaraan(merk, color)
    mobil.info()
elif jenis_kendaraan == "motor":
    merk = input("masukan merk kendaraan : ")
    color = input("masukan warna kendaraan : ")
    max_speed = int(input("masukan maximum kecepatan : "))
    bmwm1krr = SuperBike(merk, color, max_speed)
    bmwm1krr.BikeInfo()
else:
    print("jenis kendaraan tidak dikenali")