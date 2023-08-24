# Meminta pengguna memasukkan jumlah mahasiswa
jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))

# Inisialisasi list untuk menyimpan data mahasiswa
data_mahasiswa = []

# Meminta pengguna memasukkan data mahasiswa
for i in range(jumlah_mahasiswa):
    print(f"\nData Mahasiswa ke-{i+1}")
    nama = input("Nama: ")
    nim = input("NIM: ")
    nilai = []
    for j in range(5):
        nilai_mata_kuliah = float(input(f"Nilai mata kuliah ke-{j+1}: "))
        nilai.append(nilai_mata_kuliah)
    
    mahasiswa = {
        "nama": nama,
        "nim": nim,
        "nilai": nilai
    }
    data_mahasiswa.append(mahasiswa)

# Menampilkan data mahasiswa yang diinputkan
print("\nData Mahasiswa:")
for mahasiswa in data_mahasiswa:
    print(f"Nama: {mahasiswa['nama']}")
    print(f"NIM: {mahasiswa['nim']}")
    print(f"Nilai: {mahasiswa['nilai']}")
    print()
