question1 = input('Идет ли дождь? : ')
# преобразовал ответ к низшему регистру
question1 = str.lower(question1)
if question1 == 'yes':
    question2 = input('Ветренно ли на улице? : ')
    question2 = str.lower(question2)
    if question2 == 'yes':
         print('It is too windy for an umbrella')
    else:
        print('Take an umbrella')
else:
    print('Enjoy your day')