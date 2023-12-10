from pyDatalog import pyDatalog
pyDatalog.create_terms('X, Y, Z, U, W, parent, cousin')

+ parent('Анна', 'Иван')
+ parent('Анна', 'Мария')
+ parent('Ольга', 'Елена')
+ parent('Ольга', 'Алексей')
+ parent('Иван', 'Сергей')
+ parent('Елена', 'Никита')
+ parent('Алексей', 'Сергей')
+ parent('Алексей', 'Василий')

# Определение отношения 'двоюродный брат/сестра'
cousin(X, Y) <= parent(Z, X) & parent(W, Y) & parent(U, Z) & parent(U, W) & (Z != W)

# Запрос: кто является двоюродным братом или сестрой для Никиты?
print(cousin('Никита', Y))