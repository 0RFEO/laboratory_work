import math

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

# Находим среднее арифметическое кубов чисел
average_cube = (a**3 + b**3) / 2

# Находим среднее геометрическое модулей чисел
average_module = math.sqrt(abs(a) * abs(b))

print("Среднее арифметическое кубов чисел равно:", average_cube)
print("Среднее геометрическое модулей чисел равно:", average_module)