import math
a = float(input("введите длинну стороны квадрата: "))
p = a*4
print(p, ' - периметр квадрата')
a = float(input("введите длинну стороны квадрата: "))
s = a ** 2
print(s, ' - площадь квадрата')
d = a * math.sqrt(2)
print(d, ' - диагональ квадрата')
my_list = [p, s, d]
print(my_list)