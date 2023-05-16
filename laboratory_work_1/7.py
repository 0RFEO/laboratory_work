a = float(input("Введите длину ребра куба: "))

# Находим площадь грани
face_area = a**2

# Находим площадь полной поверхности
total_surface_area = 6 * face_area

# Находим объем куба
volume = a**3

print("Площадь грани куба равна:", face_area)
print("Площадь полной поверхности куба равна:", total_surface_area)
print("Объем куба равен:", volume)