class Projector:
    def __init__(self, gedung_width, gedung_height, layar_width, layar_height):
        # Dimensi gedung (cm)
        self.gedung_width = gedung_width
        self.gedung_height = gedung_height
        # Dimensi layar (meter → cm)
        self.layar_width = layar_width * 100
        self.layar_height = layar_height * 100

    def hitung_pembesaran(self):
        # Hitung perbandingan lebar & tinggi
        scale_width = self.layar_width / self.gedung_width
        scale_height = self.layar_height / self.gedung_height
        # Ambil pembesaran proporsional (pakai skala terkecil)
        scale = min(scale_width, scale_height)
        return scale

    def tampilkan_dimensi_tampilan(self):
        scale = self.hitung_pembesaran()
        tampilan_width = self.gedung_width * scale
        tampilan_height = self.gedung_height * scale
        return tampilan_width, tampilan_height, scale

    def tampilkan_hasil(self):
        tampilan_width, tampilan_height, scale = self.tampilkan_dimensi_tampilan()
        print("\n=== HASIL PROYEKSI DESAIN GEDUNG ===")
        print(f"Ukuran tampilan di layar: {tampilan_width:.2f} cm x {tampilan_height:.2f} cm")
        print(f"Skala pembesaran proporsional: {scale:.2f}x")
        print(f"Atau bisa dibilang: 1 : {1/scale:.4f}")
        print("=====================================")


# ====== INPUT DARI USER ======
print("Masukkan data desain gedung dan layar proyektor!\n")
gedung_width = float(input("Lebar desain gedung (cm): "))
gedung_height = float(input("Tinggi desain gedung (cm): "))
layar_width = float(input("Lebar layar proyektor (meter): "))
layar_height = float(input("Tinggi layar proyektor (meter): "))

# Buat objek proyektor
proyektor = Projector(gedung_width, gedung_height, layar_width, layar_height)

# Tampilkan hasil
proyektor.tampilkan_hasil()