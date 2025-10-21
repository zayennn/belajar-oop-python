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


# ============= latihan 3 =============
print("\n============= latihan 3 =============")
class Products() :
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
        
class Laptop(Products) :
    def __init__(self, name, price, stock, processor):
        super().__init__(name, price, stock)
        self.processor = processor
        
class Hp(Products) :
    def __init__(self, name, price, stock, ram):
        super().__init__(name, price, stock)
        self.ram = ram
        
list_products = []

print('1. tambah produk baru')
print('2. lihat daftar list produk')
print('3. keluar dari program')

choice = int(input('pilih menu (1/2/3) : '))

if choice == 1 :
    type = input('masukan tipe produk (laptop/hp) : ').lower()
    name = input('masukan nama produk : ').capitalize()
    price = int(input('masukan harga produk : '))
    stock = int(input('masukan stock produk : '))
    
    
    if type == "laptop" :
        processor = input('masukan tipe prosesor : ').capitalize()
        product = Laptop(name, price, stock, processor)
    elif type == "hp" :
        ram = int(input('masukin jumlah kapasitas ram : '))
        product = Hp(name, price, stock, ram)
    else :
        print('produk tidak di kenali!')
    
    list_products.append(product)
    
        