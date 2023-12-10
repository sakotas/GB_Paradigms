from pyDatalog import pyDatalog
pyDatalog.create_terms('X, Y, Z, likes, has_common_interest')

+ likes('Алексей', 'Футбол')
+ likes('Игорь', 'Футбол')
+ likes('Светлана', 'Теннис')
+ likes('Василий', 'Пеннис')
+ likes('Жасмин', 'Пеннис')

has_common_interest(X, Y) <= likes(X, Z) & likes(Y, Z) & (X != Y)

# Запрос: с кем у Алексея общий интерес?
print(has_common_interest('Жасмин', X))