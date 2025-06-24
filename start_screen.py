import os

def greetings():
    print('Введите 1 для генерации пароля')
    print('Введите 2 для проверки пароля')
    answer = input()
    if answer == '1':
        os.system('python passgen.py')
    elif answer == '2':
        os.system('python checkpass.py')
    else:
        print('Введите корректное значение!')

greetings()