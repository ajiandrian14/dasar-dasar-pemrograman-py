def sequential_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Mengembalikan indeks elemen yang ditemukan
    return -1  # Mengembalikan -1 jika tidak ditemukan

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Mengembalikan indeks elemen yang ditemukan
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # Mengembalikan -1 jika tidak ditemukan

data = []

while True:
    print("\nMenu:")
    print("1. Input Data")
    print("2. Pencarian Data")
    print("3. Keluar")
    
    menu = input("Pilih menu: ")
    
    if menu == '1':
        n = int(input("Masukkan jumlah data: "))
        data = []
        for i in range(n):
            nilai = int(input(f"Masukkan data ke-{i+1}: "))
            data.append(nilai)
        print("Data berhasil dimasukkan!")
    
    elif menu == '2':
        if not data:
            print("Data belum dimasukkan.")
            continue
        target = int(input("Masukkan nilai yang ingin dicari: "))
        print("\nPencarian Berurutan:")
        result_seq = sequential_search(data, target)
        if result_seq != -1:
            print(f"Elemen {target} ditemukan di indeks {result_seq}")
        else:
            print("Elemen tidak ditemukan")
        
        print("\nPencarian Biner:")
        result_bin = binary_search(data, target)
        if result_bin != -1:
            print(f"Elemen {target} ditemukan di indeks {result_bin}")
        else:
            print("Elemen tidak ditemukan")
    
    elif menu == '3':
        print("Terima kasih!")
        break
    
    else:
        print("Menu tidak valid. Silakan pilih lagi.")