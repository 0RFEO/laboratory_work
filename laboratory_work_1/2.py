
x1 = float(input("Введите координату x первой вершины: "))
y1 = float(input("Введите координату y первой вершины: "))
x2 = float(input("Введите координату x второй вершины: "))
y2 = float(input("Введите координату y второй вершины: "))
x3 = float(input("Введите координату x третьей вершины: "))
y3 = float(input("Введите координату y третьей вершины: "))

a = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
b = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
c = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5

p = a + b + c
p /= 2

s = (p * (p - a) * (p - b) * (p - c)) ** 0.5

print("Периметр треугольника:", p * 2)
print("Площадь треугольника:", s)