total = 0
for i in range(0, 5):
     num1 = int(input('Введите число : '))
     answer = input('Добавить это число ? : ')
     if answer == "y":
          total = total + num1
print(total)


