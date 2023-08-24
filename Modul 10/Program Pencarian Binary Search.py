def binary_search(list, target):
    left = 0
    right = len(list) - 1

    while left <= right:
        mid = (left + right) // 2
        if list[mid] == target:
            return mid
        elif list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Contoh penggunaan
my_list = [2, 5, 7, 10, 18, 23, 30]
target = 5
result = binary_search(my_list, target)
if result != -1:
    print(f"Target ditemukan di indeks {result}")
else:
    print("Target tidak ditemukan")
