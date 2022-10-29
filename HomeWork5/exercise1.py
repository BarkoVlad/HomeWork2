import random
def num():
    low_number1 = int(input('Введите маленькое число : '))
    high_number2 = int(input('Введите большее число : '))
    comp_num = random.randint(low_number1, high_number2)
    return comp_num
def message():
    print('I am thinking of a number')
    hidden_number = int(input('угадайте число : '))
    return hidden_number
def check_answer(comp_num, hidden_number):
    try_again = True
    while try_again == True:
        if comp_num == hidden_number:
            print('Правильно, вы угадали')
            try_again = False
        elif comp_num > hidden_number:
            hidden_number = int(input('Вы загадали число ниже загаданного'))
        else:
            hidden_number = int(input('Вы загадали число больше загаданного'))
def main():
    comp_num = num()
    hidden_number = message()
    check_answer(comp_num, hidden_number)
main()







