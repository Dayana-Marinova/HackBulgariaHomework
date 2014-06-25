import sqlite3

conn = sqlite3.connect("store.db")
cursor = conn.cursor()

result = cursor.execute("SELECT id, name, price_per_kg, quantuty_in_kg FROM store")

for row in result:
    print(row)
