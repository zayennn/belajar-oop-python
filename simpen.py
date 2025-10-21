# ============= latihan 1 =============
print("\n============= latihan 1 =============\n")
class Mahasiswa: 
    def __init__(self, name, nim, major):
        self.name = name
        self.nim = nim
        self.major = major
        
    def info(self) :
        print("\n============= Output : =============\n")
        print(f"""nama mahasiswa                 : {self.name}
nim maahasiswa                 : {self.nim}
jurusan yang diambil mahasiswa : {self.major}""")
        
# input data mahasiswa
name = input('masukan nama mahasiswa : ').capitalize()
nim = int(input('masukan nim mahasiswa : '))
major = input('masukan jurusan yang di ambil mahasiswa : ').capitalize()

if name and nim and major :
    name = name
    nim = nim
    major = major
    data_mahasiswa = Mahasiswa(name, nim, major)
    data_mahasiswa.info()
else : 
    print('data mahasiswa tidak boleh kosong!')
    
    
# ============= latihan 2 =============
print("\n============= latihan 2 =============")
class Hewan :
    def __init__(self, name, type):
        self.name = name
        self.type = type
        
class Kucing(Hewan) :
    def __init__(self, name, type, voice):
        super().__init__(name, type)
        self.voice = voice
        
    def info(self) :
        print("============= Output : =============\n")
        print(f"""nama hewan : {self.name}
jenis hewan : {self.type}
suara hewa : {self.voice}""")
        
kucing = Kucing('Mochi', 'Kucing', 'Meow~')
kucing.info()