# latihan 1
class Buah() :
    def __init__(self, name, color):
        self.name = name
        self.color = color
        
    def info(self) :
        print(f"""
ini adalah buah : {self.name}
warna buah ini adalah : {self.color}
""")
        

apel = Buah("Apel", "Merah")
apel.info()


# latihan 2
class PersegiPanjang() :
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
    
    def hitung_luas(self) : 
        print(f"""
luas = {self.panjang * self.lebar}  
hitung keliling = {2 * (self.panjang + self.lebar)}        
""")
        
panjang = PersegiPanjang(50, 70)
panjang.hitung_luas()