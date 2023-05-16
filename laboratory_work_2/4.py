num1 = int(input())
num2 = int(input())

sum_of_numbers = num1 + num2

difference_of_numbers = num1 - num2

product_of_digits = (num1 // 100) * ((num1 % 100) // 10) * (num1 % 10) * (num2 // 100) * ((num2 % 100) // 10) * (num2 % 10)

sum_of_digits_num1 = (num1 // 100) + ((num1 % 100) // 10) + (num1 % 10)

sum_of_digits_num2 = (num2 // 100) + ((num2 % 100) // 10) + (num2 % 10)

quotient_of_sums = sum_of_digits_num1 / sum_of_digits_num2

print("Общая сумма:", sum_of_numbers)
print("Разность чисел:", difference_of_numbers)
print("Произведение цифр:", product_of_digits)
print("Частное от деления суммы цифр первого числа на сумму цифр второго числа:", quotient_of_sums)