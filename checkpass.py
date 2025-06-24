import sqlite3
import hashlib

user_password = input('Введите ваш пароль: ')

def hash_input():
    # Создание объекта хэширования
    hash_object = hashlib.sha256()

    input_encode = user_password.encode()

    # Обновление объекта хэширования данными
    hash_object.update(input_encode)

    # Получение хэша в шестнадцатеричном формате
    hex_dig = hash_object.hexdigest()
    return hex_dig

hashed_input_password = hash_input()

def check_pass():
    con = sqlite3.connect('passwords.db')
    cursor = con.cursor()
    cursor.execute('SELECT * FROM hashed_passwords WHERE (sha2) = (?)', (hashed_input_password,))
    check = cursor.fetchone()
    if check is None:
        print('Пароля нет в базе данных!')
    elif hashed_input_password in check:
        print('Пароль найден!')

check_pass()