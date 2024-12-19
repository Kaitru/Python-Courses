import sqlite3

products_connection = sqlite3.connect('Products.db')
products_cursor = products_connection.cursor()
users_connection = sqlite3.connect('Users.db')
users_cursor = users_connection.cursor()

def initiate_db():
    products_cursor.execute("""
                   CREATE TABLE IF NOT EXISTS Products (
                   id INTEGER PRIMARY KEY,
                   title TEXT NOT NULL,
                   description TEXT,
                   price INTEGER NOT NULL)
                   """)
    users_cursor.execute("""
                   CREATE TABLE IF NOT EXISTS Users (
                   id INTEGER PRIMARY KEY,
                   username TEXT NOT NULL,
                   email TEXT NOT NULL,
                   age INTEGER NOT NULL,
                   balance INTEGER NOT NULL)
    """)
    products_connection.commit()
    users_connection.commit()
    products_connection.close()
    users_connection.close()

def get_all_products():
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()
    products = cursor.execute("SELECT * FROM Products")
    connection.commit()
    connection.close()
    return products

def add_user(username, email, age):
    connection = sqlite3.connect('Users.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", 
                  (username, email, age, 1000))
    connection.commit()
    connection.close()

def is_included(username):
    connection = sqlite3.connect('Users.db')
    cursor = connection.cursor()
    user = cursor.execute("SELECT * FROM Users WHERE username = ?", 
                         (username,)).fetchone()
    connection.commit()
    connection.close()
    return bool(user)

products_connection.commit()
products_connection.close()
