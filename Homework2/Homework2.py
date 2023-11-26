# 1. Условие
# На вход подается число n.
# 2. Задача
# Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n.
# Обоснуйте выбор парадигм.
# 3. Пример вывода:
# 1 * 1 = 1
# 1 * 2 = 2
# 1 * 3 = 3
# 1 * 4 = 4
# 1 * 5 = 5
# 1 * 6 = 6
# ..
# 1 * 9 = 9

def multiplication_table(n):
    """
    Функция для вывода таблицы умножения для чисел от 1 до n.

    Параметры:
    n (int): верхний предел для таблицы умножения.

    Возвращает:
    str: Строка с таблицей умножения.
    """
    result = ""
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            result += f"{i} * {j} = {i * j}\n"
        result += "\n"  # Добавляем пустую строку для разделения строк таблицы
    return result

# Пример использования функции
if __name__ == "__main__":
    # Выводим таблицу умножения для чисел от 1 до 5
    print(multiplication_table(5))

    # Для демонстрации выводим также таблицу умножения для чисел от 1 до 3
    print("Таблица умножения для чисел от 1 до 3:")
    print(multiplication_table(3))
