my_list = [1, 1.0, 2, 2, 5.0, "python", "python3", "python3"]
print(my_list)
my_list_poped = my_list.pop(2)
print(my_list_poped)
my_list_poped_ = my_list.pop(3)
print(my_list_poped_)
my_list_poped__ = my_list.pop(4)
print(my_list_poped__)
my_list = [my_list_poped, my_list_poped_, my_list_poped__]
print(my_list)
# с помощью команды reverce() выводим список в обратном порядке
my_list.reverse()
print(my_list)