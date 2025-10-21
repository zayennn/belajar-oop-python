# ============= latihan 1 =============
class Mahasiswa: 
    def __init__(self, name, nim, major):
        self.name = name
        self.nim = nim
        self.major = major
        
    def info(self) :
        print("============= latihan 1 =============")
        print(f"")
        
mahasiswa = Mahasiswa('test', 123, 'test')
mahasiswa.info()