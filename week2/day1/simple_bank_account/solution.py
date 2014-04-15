balance = 100


def get_balance():
    global balance
    if balance < 0:
        return False
    return balance


def deposit_money(amount):
    global balance
    if amount < 0:
        return False
    balance += amount
    return balance


def withdraw_money(amount):
    global balance
    if amount < 0 or balance < amount:
        return False
    balance -= amount
    return balance
