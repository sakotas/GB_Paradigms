from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, sum_list')

# Определение предиката sum_list, который суммирует элементы списка
@pyDatalog.predicate()
def sum_list(lst):
    return sum(y for (_, y) in lst)

# Функция для суммирования элементов списка
def sum_elements_of_list(input_list):
    # Преобразование списка в список пар индекс-значение
    indexed_list = list(enumerate(input_list))
    # Вызов предиката sum_list с индексированным списком
    sum_result = sum_list(indexed_list)
    # Возврат суммы элементов списка
    return sum_result

# Пример использования
example_list = [1, 2, 3, 4, 5]
print(sum_elements_of_list(example_list))
