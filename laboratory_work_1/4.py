first_term = int(input("Введите первый член арифметической прогрессии: "))
common_diff = int(input("Введите знаменатель арифметической прогрессии: "))
num_terms = int(input("Введите количество членов арифметической прогрессии: "))

sum_terms = ((2 * first_term) + (common_diff * (num_terms - 1))) * num_terms / 2

print("Сумма членов арифметической прогрессии равна:", sum_terms)