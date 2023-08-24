def insertion_sort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        
        while j >= 0 and list[j] > key:
            list[j + 1] = list[j]
            j = j - 1
        
        list[j + 1] = key

# Contoh penggunaan
my_list = [12, 5, 8, 9, 3, 15, 7]
insertion_sort(my_list)
print("List yang sudah diurutkan:", my_list)
