my_list = [1, 1.0, 2, 2, 5.0, "python", "python3", "python3"]
# узнать количество элементов через len
num1 = len(my_list)
print(num1)
# узнал количество уникальных элементов
num2 = set(my_list)
print(num2)
# узнал количество элементов в set
num3 = len(num2)
# узнал разницу
dif = num1 - num3
print(dif)