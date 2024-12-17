import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS Users (
               id INTEGER PRIMARY KEY,
               username TEXT NOT NULL,
               email TEXT NOT NULL,
               age INTEGER,
               balance INTEGER NOT NULL)""")

for i in range(10):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f"user{i + 1}", f"example{i + 1}@gmail.com", str((i + 1) * 10), str(1000)))

cursor.execute("UPDATE Users SET balance = balance - 500 WHERE id % 2 != 0")

cursor.execute("DELETE FROM Users WHERE id % 3 == 1")

cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")
users = cursor.fetchall()
for user in users:
    print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')

connection.commit()
connection.close()
