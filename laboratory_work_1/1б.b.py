import math
x = float(input())
y = float(input())
print(1 + math.fabs(y - x) + ((y - x * x)/ 2) + (math.pow(math.fabs(y - x), 3) / 3))