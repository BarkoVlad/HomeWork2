num1 = int(input('Введите число > 20 это в прямом направлении, если < 20 то,  в обратном направлении  : '))
if num1 > 20:
    for i in range(1, num1 + 1):
        print(i)
elif num1 < 20:
    for i in range(20, num1-1, -1):
        print(i)
else:
    print("I don't understand")

