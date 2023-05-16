import math
x = float(input())
y = float(input())
print((math.sqrt(math.fabs(x - 1)) - math.fabs(y ** (1. / 3.))) / (1 + (x*x)/2 + (y*y)/4))