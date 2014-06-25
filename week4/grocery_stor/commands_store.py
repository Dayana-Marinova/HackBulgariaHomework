import sqlite3
from collections import OrderedDict
from create_store import insert, insert_customers
import json


class Store():
      """docstring for store"""
    def __init__(self):
        self.conn = sqlite3.connect("store.db")
        self.store = self.conn.cursor()

    def import_products_json(self, file_name):
        f = open(file_name, "r")

        for lines in json.load(f):
            insert(lines, self.store)
        f.close()

        self.conn.commit()

    def list_products(self):
        result = "SELECT id, name, price_per_kg, quantity_in_kg  FROM store")
        for row in result:
            print('[' + str(row[0]) + '] ' + row[1] + ' - ' + str(row[2]) + ' BGN - ' + str(row[3]) + ' kg')

    def add_product(self):
        name = input('Name> ')
        price_per_kg = input('price_per_kg> ')
        quantity_in_kg = input('quantity_in_kg> ')

        query_store = "INSERT INTO store VALUES(NULL, ?, ?, ?)"
        self.store.execute(query_store, (name, price_per_kg, quantity_in_kg))

    def delete_product(self, id_of_product):
        self.store.execute("DELETE FROM store WHERE id = ?", (id_of_product,))

        self.conn.commit()

    def update_product(self, id_of_product):
        name = input('Name> ')
        price_per_kg = input('price_per_kg> ')
        quantity_in_kg = input('quantity_in_kg> ')

        guery_store = "UPDATE store SET name = ?, price_per_kg = ?, quantity_in_kg = ? WHERE id = ?"
        self.store.execute(guery_store, (name, price_per_kg, quantity_in_kg, id_of_product))

        self.conn.commit()

    def export_products_json(self, file_name):
        output = []
        json_contents = self.store.execute("SELECT name, price_per_kg, quantity_in_kg FROM store;").fetchall()
        for row in json_contents:
            json_record = {}
            json_record["name"] = row[0]
            json_record["price_per_kg"] = row[1]
            json_record["quantity_in_kg"] = row[2]
            output.append(json_record)
        f = open(file_name, "w")
        json_contents = json.dumps(output, sort_keys=True, indent=4)
        f.write(json_contents)
        f.close()

    def import_customers_json(self, file_name):
        f = open(file_name, "r")

        for lines in json.load(f):
            insert_customers(lines, self.store)
        f.close()

        self.conn.commit()

    def list_customers(self):
        result = self.store.execute("SELECT id, name, kg_bought, money_spent  FROM customers")
        for row in result:
            print('[' + str(row[0]) + '] ' + row[1] + ' - ' + str(row[2]) + ' kg - ' + str(row[3]) + ' BGN')

    def add_customer(self):
        name = input('Name> ')
        kg_bought = input('kg_bought> ')
        money_spent = input('money_spent> ')

        query_store = "INSERT INTO customers VALUES(NULL, ?, ?, ?)"
        self.store.execute(query_store, (name, kg_bought, money_spent))

    def delete_customer(self, id_of_customer):
        self.store.execute("DELETE FROM customers WHERE id = ?", (id_of_customer,))

        self.conn.commit()

    def update_customer(self, id_of_customer):
        name = input('Name> ')
        kg_bought = input('kg_bought> ')
        money_spent = input('money_spent> ')

        guery_store = "UPDATE customers SET name = ?, kg_bought = ?, money_spent = ? WHERE id = ?"
        self.store.execute(guery_store, (name, kg_bought, money_spent, id_of_customer))

        self.conn.commit()

    def export_customers_json(self, file_name):
        output = []
        json_contents = self.store.execute("SELECT name, kg_bought, money_spent FROM customers;").fetchall()
        for row in json_contents:
            json_record = OrderedDict()
            json_record["name"] = row[0]
            json_record["kg_bought"] = row[1]
            json_record["money_spent"] = row[2]
            output.append(json_record)
        f = open(file_name, "w")
        json_contents = json.dumps(output, indent=4)
        f.write(json_contents)
        f.close()

    def buy(id_of_customer):
        pass
        


def main():
    store = Store()
    while True:
        command = input("Enter command>>")
        command_array = command.split(" ")
        if command_array[0] == 'import_products_json':
            store.import_products_json(command_array[1])
        elif command_array[0] == 'list_products':
            store.list_products()
        elif command_array[0] == 'add_product':
            store.add_product()
        elif command_array[0] == 'delete_product':
            store.delete_product(command_array[1])
        elif command_array[0] == 'update_product':
            store.update_product(command_array[1])
        elif command_array[0] == 'export_products_json':
            store.export_products_json(command_array[1])
        elif command_array[0] == 'import_customers_json':
            store.import_customers_json(command_array[1])
        elif command_array[0] == 'list_customers':
            store.list_customers()
        elif command_array[0] == 'add_customer':
            store.add_customer()
        elif command_array[0] == 'delete_customer':
            store.delete_customer(command_array[1])
        elif command_array[0] == 'update_customer':
            store.update_customer(command_array[1])
        elif command_array[0] == 'export_customers_json':
            store.export_customers_json(command_array[1])
        elif command_array[0] == 'buy':
            store.buy(command_array[1])

if __name__ == '__main__':
    main()
