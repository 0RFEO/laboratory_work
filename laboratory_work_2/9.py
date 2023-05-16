a = int(input())
b = int(input())

result = (a % b == 0) or (b % a == 0)

if result:
    print(1)
else:
    print(2)