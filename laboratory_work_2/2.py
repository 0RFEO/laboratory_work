oklad = float(input())
stavka = float(input())
podohodny_nalog = oklad * stavka / 100
summa_na_ruki = oklad - podohodny_nalog

print("Размер подоходного налога:", podohodny_nalog, "руб.")
print("Сумма, получаемая на руки:", summa_na_ruki, "руб.")