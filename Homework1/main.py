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


if __name__ == "__main__":
    # Пример использования обеих функций:
    example_list = [64, 34, 25, 12, 22, 11, 90]

    sorted_imperative = sort_list_imperative(example_list.copy())
    print("Императивно отсортированный список:", sorted_imperative)

    sorted_declarative = sort_list_declarative(example_list.copy())
    print("Декларативно отсортированный список:", sorted_declarative)
