import timeit


# Структурный подход
def binary_search_structural(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# Процедурный подход
def binary_search_procedural(arr, target):
    def search(low, high):
        if low > high:
            return -1
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return search(mid + 1, high)
        else:
            return search(low, mid - 1)

    return search(0, len(arr) - 1)


# Объектно-ориентированный подход
class BinarySearchOOP:
    def __init__(self, arr):
        self.arr = arr

    def search(self, target):
        low, high = 0, len(self.arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.arr[mid] == target:
                return mid
            elif self.arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1


# Пример использования
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
targets = [9, 13, 20]  # Дополнительные цели для поиска

# Структурный поиск
start_time = timeit.default_timer()
for target in targets:
    index_structural = binary_search_structural(arr, target)
    print(f"Структурный подход: Индекс числа {target} равен {index_structural}")
end_time = timeit.default_timer()
print(f"Структурный поиск занял {((end_time - start_time) * 1e6):.3f} микросекунд\n")

# Процедурный поиск
start_time = timeit.default_timer()
for target in targets:
    index_procedural = binary_search_procedural(arr, target)
    print(f"Процедурный подход: Индекс числа {target} равен {index_procedural}")
end_time = timeit.default_timer()
print(f"Процедурный поиск занял {((end_time - start_time) * 1e6):.3f} микросекунд\n")

# Объектно-ориентированный поиск
start_time = timeit.default_timer()
searcher = BinarySearchOOP(arr)
for target in targets:
    index_oop = searcher.search(target)
    print(f"ООП подход: Индекс числа {target} равен {index_oop}")
end_time = timeit.default_timer()
print(f"ООП поиск занял {((end_time - start_time) * 1e6):.3f} микросекунд\n")
