import sqlite3


def create_table(store):
    store.execute('''CREATE TABLE store
        (id INTEGER PRIMARY KEY, name text, price_per_kg real, quantity_in_kg int)''')
    store.execute('''CREATE TABLE customers
        (id INTEGER PRIMARY KEY, name text, kg_bought real, money_spent real)''')


def insert_customers(item, store):
    name = item['name']
    kg_bought = item['kg_bought']
    money_spent = item['money_spent']

    guery_store = "INSERT INTO customers VALUES(NULL, ?, ?, ?)"
    store.execute(guery_store, (name, kg_bought, money_spent))


def insert(item, store):
    name = item["name"]
    price_per_kg = item["price_per_kg"]
    quantity_in_kg = item['quantity_in_kg']

    query_store = "INSERT INTO store VALUES(NULL, ?, ?, ?)"
    store.execute(query_store, (name, price_per_kg, quantity_in_kg))

data = [{
    "name": "Potatoes",
    "price_per_kg": 1.2,
    "quantity_in_kg": 20,
}, {
    "name": "Carrots",
    "price_per_kg": 1.1,
    "quantity_in_kg": 6,
}, {
    "name": "Cucumbers",
    "price_per_kg": 2.2,
    "quantity_in_kg": 3,
}, {
    "name": "Lettuce",
    "price_per_kg": 2.1,
    "quantity_in_kg": 7,
}, {
    "name": "Tomatoes",
    "price_per_kg": 2.7,
    "quantity_in_kg": 10,
}]


def create_database(file_name, fake):
    conn = sqlite3.connect(file_name)
    c = conn.cursor()

    try:
        create_table(c)
    except Exception:
        return "Allready exists"
    if fake:
        for item in data:
            insert(item, c)

    conn.commit()
    conn.close()


def main():
    create_database('store.db', False)

if __name__ == '__main__':
    main()
