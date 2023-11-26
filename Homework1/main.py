import unittest

def sort_list_imperative(numbers):
    """
    Сортировка списка чисел в порядке убывания, используя императивный подход.

    Алгоритм сортировки: пузырьковая сортировка.

    Параметры:
    numbers (list): список целых чисел.

    Возвращает:
    list: отсортированный по убыванию список чисел.
    """
    # Реализация алгоритма сортировки пузырьком
    n = len(numbers)
    for i in range(n):
        # Последние i элементов уже на месте
        for j in range(0, n - i - 1):
            if numbers[j] < numbers[j + 1]:  # Для убывающего порядка используется <
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


def sort_list_declarative(numbers):
    """
    Сортировка списка чисел в порядке убывания, используя декларативный подход.

    Используется встроенная функция sorted() для сортировки списка.

    Параметры:
    numbers (list): список целых чисел.

    Возвращает:
    list: отсортированный по убыванию список чисел.
    """
    # Декларативный код с использованием встроенной функции сортировки Python
    return sorted(numbers, reverse=True)


# # Класс юнит-теста
# class TestSortingMethods(unittest.TestCase):
#     def test_sort_list_imperative(self):
#         self.assertEqual(sort_list_imperative([12, 4, 5, 6, 7]), [12, 7, 6, 5, 4])
#         self.assertEqual(sort_list_imperative([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])
#         self.assertEqual(sort_list_imperative([]), [])
#
#     def test_sort_list_declarative(self):
#         self.assertEqual(sort_list_declarative([12, 4, 5, 6, 7]), [12, 7, 6, 5, 4])
#         self.assertEqual(sort_list_declarative([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])
#         self.assertEqual(sort_list_declarative([]), [])


if __name__ == "__main__":
    # Пример использования обеих функций:
    example_list = [64, 34, 25, 12, 22, 11, 90]

    sorted_imperative = sort_list_imperative(example_list.copy())
    print("Императивно отсортированный список:", sorted_imperative)

    sorted_declarative = sort_list_declarative(example_list.copy())
    print("Декларативно отсортированный список:", sorted_declarative)
