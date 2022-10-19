firstname = input('Введите имя : ')
if len(firstname) < 5:
    surname = input('Введите фамилию : ')
    name = firstname+surname
    print(name.upper())
else:
    print(firstname.lower())

