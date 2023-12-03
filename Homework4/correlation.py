import numpy as np
from typing import List


def pearson_correlation(x: List[float], y: List[float]) -> float:
    """
    Вычисляет коэффициент корреляции Пирсона между двумя массивами.

    Параметры:
    x (List[float]): Первый массив случайных величин.
    y (List[float]): Второй массив случайных величин.

    Возвращает:
    float: Коэффициент корреляции Пирсона между двумя массивами.

    Исключения:
    ValueError: Если один из массивов пуст или если элементы массивов не являются числами.

    Примеры:
    >>> pearson_correlation([1, 2, 3], [4, 5, 6])
    1.0
    >>> pearson_correlation([1, 2, 3], [3, 2, 1])
    -1.0
    """
    if not all(isinstance(n, (int, float)) for n in x + y):
        raise ValueError("Все элементы массивов должны быть числами.")

    # Преобразование списков в массивы numpy для быстрых вычислений
    x_array = np.array(x)
    y_array = np.array(y)

    # Проверка на пустые массивы
    if x_array.size == 0 or y_array.size == 0:
        raise ValueError("Массивы не должны быть пустыми.")

    # Средние значения для каждого массива
    mean_x = np.mean(x_array)
    mean_y = np.mean(y_array)

    # Вычисление числителя коэффициента корреляции Пирсона
    numerator = np.sum((x_array - mean_x) * (y_array - mean_y))

    # Вычисление знаменателя коэффициента корреляции Пирсона
    denominator = np.sqrt(np.sum((x_array - mean_x) ** 2) * np.sum((y_array - mean_y) ** 2))

    # Вычисление коэффициента корреляции Пирсона
    correlation = numerator / denominator if denominator else 0.0

    return correlation


# Примеры использования функции с проверкой
try:
    print(pearson_correlation([1, 2, 'a'], [4, 5, 6]))  # Вызовет исключение
except ValueError as e:
    print(e)

try:
    print(pearson_correlation([], [4, 5, 6]))  # Вызовет исключение
except ValueError as e:
    print(e)

try:
    print(pearson_correlation([1, 2, 3], [4, 5, 6]))  # Корректные данные
except ValueError as e:
    print(e)
