import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

# cursor.execute("""
#                CREATE TABLE IF NOT EXISTS Users (
#                id INTEGER PRIMARY KEY,
#                username TEXT NOT NULL,
#                email TEXT NOT NULL,
#                age INTEGER,
#                balance INTEGER NOT NULL)""")
#
# for i in range(10):
#     cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f"user{i + 1}", f"example{i + 1}@gmail.com", str((i + 1) * 10), str(1000)))
#
# cursor.execute("UPDATE Users SET balance = balance - 500 WHERE id % 2 != 0")
#
# cursor.execute("DELETE FROM Users WHERE id % 3 == 1")
#
# cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")
# users = cursor.fetchall()
# for user in users:
#     print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')

# cursor.execute("DELETE FROM Users WHERE id == 6")

cursor.execute("SELECT COUNT(*) FROM Users")
users_count = cursor.fetchone()[0]
print(users_count)

cursor.execute("SELECT SUM(balance) FROM Users")
sum_balance = cursor.fetchone()[0]
print(sum_balance)

cursor.execute("SELECT AVG(balance) FROM Users")
avg_balance = cursor.fetchone()[0]
print(avg_balance)

connection.commit()
connection.close()
