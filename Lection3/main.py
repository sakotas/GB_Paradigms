import pandas as pd
import math

print(type(dir(pd.DataFrame)))


# for i in dir(pd.DataFrame):
#     print(i)

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        self.area = self.height * self.width
        return self.area

r = Rectangle(4,5)

print(r)

print(r.height)
print(r.width)

print(r.area())

