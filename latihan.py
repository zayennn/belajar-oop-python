# ============= latihan 1 =============
class Mahasiswa: 
    def __init__(self, name, nim, major):
        self.name = name
        self.nim = nim
        self.major = major
        
    def info(self) :
        print("\n============= latihan 1 =============\n")
        print(f"")
        
mahasiswa = Mahasiswa('test', 123, 'test')
mahasiswa.info()