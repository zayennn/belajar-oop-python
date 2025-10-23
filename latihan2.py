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