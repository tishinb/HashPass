'''
Программу для генерации паролей (обязательные пункты: пароль должен хэшироваться, помещаться в sqlite3, если
мы пытаемся получить захешированный пароль из БД, мы должны сначала его расхешировать. Тип хэша выбирайте сами)
'''

import sqlite3
import random
import string
import hashlib



def create_table():
    con = sqlite3.connect('passwords.db')
    cursor = con.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS hashed_passwords (
            id INTEGER PRIMARY KEY NOT NULL,
            sha2 TEXT NOT NULL
        )
    ''')
    con.commit()
    con.close()
    print('Таблица создана')

create_table()

# Предопределенные наборы символов
ascii_lowercase = string.ascii_lowercase
ascii_uppercase = string.ascii_uppercase
digits = string.digits
punctuation = string.punctuation

# Вывод доступных наборов символов
print("ascii_lowercase: ", ascii_lowercase)
print("ascii_uppercase: ", ascii_uppercase)
print("digits: ", digits)
print("punctuation: ", punctuation)

# Ввод параметров пароля
password_length = int(input("Введите длину пароля: "))
uppercase_letters = input("Включить буквы верхнего регистра? (y/n): ").lower()
lowercase_letters = input("Включить буквы нижнего регистра? (y/n): ").lower()
digits_set = input("Включить цифры? (y/n): ").lower()
special_symbols = input("Включить специальные символы? (y/n): ").lower()

# Проверка ввода и настройка флагов
def check_input():
    if password_length <= 0:
        print("Некорректная длина пароля!")
        return False

    valid_inputs = {'y', 'n'}
    if (
            uppercase_letters not in valid_inputs or
            lowercase_letters not in valid_inputs or
            digits_set not in valid_inputs or
            special_symbols not in valid_inputs
    ):
        print("Некорректный ввод (должно быть 'y' или 'n')!")
        return False

    return True


if not check_input():
    exit()


# Генерация пароля
def password_generator():
    password_values = []

    if uppercase_letters == 'y':
        password_values += ascii_uppercase
    if lowercase_letters == 'y':
        password_values += ascii_lowercase
    if digits_set == 'y':
        password_values += digits
    if special_symbols == 'y':
        password_values += punctuation

    if not password_values:
        print("Не выбраны символы для генерации пароля!")
        exit()

    return "".join(random.sample(password_values, password_length))


# Генерация и вывод пароля
password = password_generator()
print("Сгенерированный пароль:", password)

def password_hash():
    # Создание объекта хэширования
    hash_object = hashlib.sha256()

    input_encode = password.encode()

    # Обновление объекта хэширования данными
    hash_object.update(input_encode)

    # Получение хэша в шестнадцатеричном формате
    hex_dig = hash_object.hexdigest()
    return hex_dig

hashed_password = password_hash()

def add_password2db():
    con = sqlite3.connect('passwords.db')
    cursor = con.cursor()
    cursor.execute('INSERT INTO hashed_passwords (sha2) VALUES (?)', (hashed_password,))
    # Сохраняем изменения и закрываем соединение
    con.commit()
    con.close()
    print('Пароль добавлен!')

add_password2db()
