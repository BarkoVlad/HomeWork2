num1 = int(input('Введите первое число : '))
total = num1
again = "y"
while again == "y":
    num2 = int(input("Введите второе число : "))
    total = total + num2
    again = input("Хотите ввести еще одно число? (y/n) : ")
print("The total is", total)