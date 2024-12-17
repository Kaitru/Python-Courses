import sqlite3

connection = sqlite3.connect('Products.db')
cursor = connection.cursor()

def initiate_db():
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS Products (
                   id INTEGER PRIMARY KEY,
                   title TEXT NOT NULL,
                   description TEXT,
                   price INTEGER NOT NULL)
                   """)
    connection.commit()

def get_all_products():
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()
    products = cursor.execute("SELECT * FROM Products")
    connection.commit()
    return products

connection.commit()
connection.close()
