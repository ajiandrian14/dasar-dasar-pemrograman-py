class NilaiMataKuliah:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
        self.nilai_kuis = []
        self.nilai_tugas = []
        self.nilai_uts = 0
        self.nilai_uas = 0
    
    def tambah_nilai_kuis(self, nilai):
        self.nilai_kuis.append(nilai)
    
    def tambah_nilai_tugas(self, nilai):
        self.nilai_tugas.append(nilai)
    
    def tambah_nilai_uts(self, nilai):
        self.nilai_uts = nilai
    
    def tambah_nilai_uas(self, nilai):
        self.nilai_uas = nilai
    
    def hitung_nilai_akhir(self):
        rata_nilai_kuis = sum(self.nilai_kuis) / len(self.nilai_kuis)
        rata_nilai_tugas = sum(self.nilai_tugas) / len(self.nilai_tugas)
        
        nilai_akhir = 0.2 * rata_nilai_kuis + 0.1 * rata_nilai_tugas + 0.35 * self.nilai_uts + 0.35 * self.nilai_uas
        return nilai_akhir

# Membuat objek NilaiMataKuliah
nama_mahasiswa = input("Masukkan nama mahasiswa: ")
nim_mahasiswa = input("Masukkan NIM mahasiswa: ")
nilai_mata_kuliah = NilaiMataKuliah(nama_mahasiswa, nim_mahasiswa)

# Memasukkan nilai-nilai
for i in range(2):
    nilai_kuis = float(input(f"Masukkan nilai kuis ke-{i+1}: "))
    nilai_mata_kuliah.tambah_nilai_kuis(nilai_kuis)

for i in range(3):
    nilai_tugas = float(input(f"Masukkan nilai tugas ke-{i+1}: "))
    nilai_mata_kuliah.tambah_nilai_tugas(nilai_tugas)

nilai_uts = float(input("Masukkan nilai UTS: "))
nilai_mata_kuliah.tambah_nilai_uts(nilai_uts)

nilai_uas = float(input("Masukkan nilai UAS: "))
nilai_mata_kuliah.tambah_nilai_uas(nilai_uas)

# Menghitung dan menampilkan nilai akhir
nilai_akhir = nilai_mata_kuliah.hitung_nilai_akhir()
print(f"Nama: {nilai_mata_kuliah.nama}")
print(f"NIM: {nilai_mata_kuliah.nim}")
print(f"Nilai Akhir: {nilai_akhir:.2f}")
