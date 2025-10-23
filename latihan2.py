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


# latihan 3
class NilaiMahasiswa() :
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def check_kelulusan(self) :
        print(f"""
nama mahasiswa : {self.name}
nilai mahasiswa : {self.score}
status mahasiswa : {"lulus" if self.score >= 60 else "tidak lulus"}
""")
        
nama_mahasiswa = input('masukan nama mahasiswa : ').capitalize()
nilai = int(input('masukan nilai : '))

mahasiswa = NilaiMahasiswa(nama_mahasiswa, nilai)
mahasiswa.check_kelulusan()


# latihan 4
class Kendaraan() :
    def __init__(self, merk, year):
        self.merk = merk
        self.year = year
        
class JumlahPintu (Kendaraan) :
    def __init__(self, merk, year, jumlah_pintu):
        super().__init__(merk, year)
        
        self.jumlah_pintu = jumlah_pintu
        
    def info_kendaraan(self) :
        print(f"""
merk kendaraan : {self.merk}
tahun keluaran : {self.year}
jumlah pintu mobil : {self.jumlah_pintu}              
""")
        
        
bmwm2 = JumlahPintu("BMW M2", "2024", 2)
bmwm2.info_kendaraan()