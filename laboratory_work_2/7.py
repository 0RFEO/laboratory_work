num = input("Введите число: ")
for i in range(len(num)):
    for j in range(len(num)):
        if i != j:
            for k in range(len(num)):
                if k != i and k != j:
                    print(num[i] + num[j] + num[k])