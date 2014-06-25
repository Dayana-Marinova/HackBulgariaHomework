import sqlite3
from Client import Client
from time import time
from getpass import getpass
import hashlib
import smtplib
import random

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()


def create_clients_table():
    create_query = '''create table if not exists
        clients(id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT,
                balance REAL DEFAULT 0,
                message TEXT,
                the_time_of_last INTEGER DEFAULT 0,
                email TEXT,
                message_code TEXT,
                count_tan DEFAULT 0)'''

    cursor.execute(create_query)


def create_tan_codes_table():
    create_query = '''create table if not exists
        tan(id_client INTEGER,
            code TEXT,
            used BOOLEAN)'''

    cursor.execute(create_query)


def change_message(new_message, logged_user):
    update_sql = "UPDATE clients SET message = ? WHERE id = ?"
    cursor.execute(update_sql, (new_message, logged_user.get_id()))
    conn.commit()
    logged_user.set_message(new_message)


def change_pass(new_pass, logged_user):
    update_sql = "UPDATE clients SET password = ? WHERE id = ?"
    cursor.execute(update_sql, (new_pass, logged_user.get_id()))
    conn.commit()


def register(username, password, email):
    insert_sql = "insert into clients (username, password, email) values (?, ?, ?)"
    cursor.execute(insert_sql, (username, password, email))
    conn.commit()
1

def login(username, password):
    select_query = "SELECT id, username, email, balance, message FROM clients WHERE username = ? AND password = ? LIMIT 1"
    cursor.execute(select_query, (username, password))
    user = cursor.fetchone()

    if(user):
        return Client(user[0], user[1], user[2], user[3], user[4])
    else:
        return False


def get_password(username):
    select_query = "SELECT password FROM clients WHERE username = ?"
    cursor.execute(select_query, (username, ))
    result = cursor.fetchone()

    return result[0]


def wrong_password_count(username):
    count = 1

    password = getpass()

    while get_crypted(password) != get_password(username):
        if not if_the_user_block(username):
            count += 1
            password = getpass()
            if get_crypted(password) == get_password(username):
                return get_crypted(password)
            elif count % 5 == 0:
                time_block_wrong_password(username)
        else:
            print('you are blocked')
            return False
    else:
        return get_crypted(password)


def get_email(username):
    select_query = 'SELECT email FROM clients WHERE username = ?'
    cursor.execute(select_query, (username, ))
    result = cursor.fetchone()

    return result[0]


def time_block_wrong_password(username):
    now = int(time())

    select_query = 'UPDATE clients SET the_time_of_last = (?) WHERE username = (?)'
    cursor.execute(select_query, (now, username))
    conn.commit()

    print('try again after 5 min')
    return True


def if_the_user_block(username):
    now = int(time())

    select_query = 'SELECT the_time_of_last FROM clients WHERE username = (?)'
    cursor.execute(select_query, (username, ))
    result = cursor.fetchone()

    the_time = int(result[0])

    if now <= the_time + 300:
        return True
    return False


def get_crypted(password):
    pw = password.encode('utf-8')
    h = hashlib.sha1()
    h.update(pw)
    crypted = h.hexdigest()
    return crypted


def send_massage(message, username):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("dayanamarinova1993@gmail.com", "lubomirova70")
    server.sendmail("dayanamarinova@gmail.com", get_email(username), message)
    server.quit()
    return 'send email'
    print


def send_reset_password(username):
    message = message_hash()
    set_code(message, username)
    print(send_massage(message, username))


def set_code(message, username):
    select_query = 'UPDATE clients SET message_code = ? WHERE username = ?'
    cursor.execute(select_query, (message, username))
    conn.commit()


def get_code(username):
    select_query = 'SELECT message_code FROM clients WHERE username = ?'
    cursor.execute(select_query, (username, ))
    result = cursor.fetchone()

    return result[0]


def message_hash():
    return hashlib.sha1(str(random.random()).encode('utf-8')).hexdigest()


def reset_password(username):
    code = input('Enter your code: ')
    if code == get_code(username):
        new_password = getpass.getpass()
        password = get_crypted(new_password)
        select_query = 'UPDATE clients SET password = (?) WHERE username = (?)'
        cursor.execute(select_query, (password, username))
        conn.commit()
        return 'successfully change your password'
    else:
        return 'the code is incorrect'


def get_balance(username):
    select_query = 'SELECT balance FROM clients WHERE username = ?'
    cursor.execute(select_query, (username, ))
    result = cursor.fetchone()

    return result[0]


def update_balance(username, balance):
    select_query = 'UPDATE clients SET balance = ? WHERE username = ?'
    cursor.execute(select_query, (balance, username))
    conn.commit()
    return 'updated'


def get_tan(tan):
    select_query = 'SELECT used FROM tan WHERE code = ?'
    cursor.execute(select_query, (tan,))
    result = cursor.fetchone()

    return result[0]


def update_tan(tan):
    select_query = 'UPDATE tan SET used = 1 WHERE code = ?'
    cursor.execute(select_query, (tan, ))
    conn.commit()

    return 'code is used'


def get_count_tan(username):
    select_query = 'SELECT count_tan FROM clients WHERE username = ?'
    cursor.execute(select_query, (username, ))
    result = cursor.fetchone()

    return result[0]


def update_count_tan(username, count):
    count_tan = get_count_code(username) - count
    select_query = 'UPDATE clients SET count_tan = ? WHERE username = ?'
    cursor.execute(select_query, (username, count_tan))
    conn.commit()

    return 'update count tan'


def deposit(username, amount, tan):
    if get_tan(tan) == 0:
        balance = get_balance(username) + float(amount)
        update_balance(username, balance)
        update_tan(tan)
        update_count_tan(username, 1)
        return 'Transaction successful! \n %s were deposited to the bank' % amount
    else:
        return 'I`m sorry tan is used or wrong'


def withdraw(username, amount, tan):
    if get_tan(tan) == 0:
        if float(amount) > get_balance(username):
            return 'You don`t have enough money in the bank'
        else:
            balance = get_balance(username) - float(amount)
            update_balance(username, balance)
            update_tan(tan)
            update_count_tan(username, 1)
            return 'withdraw was successful'
    else:
        return 'I`m sorry tan is used or wrong'


def get_email_by_password(password):
    select_query = 'SELECT email FROM clients WHERE password = ?'
    cursor.execute(select_query, (get_crypted(password), ))
    result = cursor.fetchone()

    return result[0]


def get_count_code(username):
    select_query = 'SELECT count_tan FROM clients WHERE username = ?'
    cursor.execute(select_query, (username, ))
    result = cursor.fetchone()

    return result[0]


def generate_tan_codes(username, password):
    if get_count_code(username) != 0:
        return get_count_code(username)
    array_tan_codes = []
    if get_crypted(password) != get_password(username):
        return 'Wrong password'
    else:
        i = 1
        while i <= 10:
            code = message_hash()[:32]
            array_tan_codes.append(code)
            add_code_with_username(code, username)
            i += 1
    message = ''
    for code in array_tan_codes:
        message += code + '\n'
    print(send_massage(message, username))
    print(update_tan_count_10(username))
    return 'codes are generate'


def update_tan_count_10(username):
    select_query = 'UPDATE clients SET count_tan = 10 WHERE username = ?'
    cursor.execute(select_query, (username, ))
    conn.commit()

    return 'count is start again'


def get_id(username):
    select_query = 'SELECT id FROM clients WHERE username = ?'
    cursor.execute(select_query, (username, ))
    result = cursor.fetchone()

    return result[0]


def add_code_with_username(code, username):
    create_tan_codes_table()
    select_query = 'INSERT INTO tan VALUES (?, ?, ?)'
    cursor.execute(select_query, (get_id(username), code, False))
    conn.commit()
