import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL)
''')
for i in range(10):
    cursor.execute("INSERT INTO Users (id, username, email, age, balance) VALUES (?, ?, ?, ?, ?)",
                (i + 1, f'User{i}', f'example{i}@gmail.com', (i + 1) * 10, 1000))

cursor.execute("SELECT * FROM Users")
rows = cursor.fetchall()


for row in rows[::2]:
    cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", (500, row[0],))


for row in rows[::3]:
    cursor.execute("DELETE FROM Users WHERE id = ?", (row[0],))


cursor.execute("SELECT * FROM Users WHERE age != ?", (60,))
row_age = cursor.fetchall()

cursor.execute("DELETE FROM Users WHERE id = ?", (6,))


cursor.execute("SELECT COUNT(*) FROM Users")
count_us = cursor.fetchone()[0]


cursor.execute("SELECT SUM(balance) FROM Users")
balance_sum = cursor.fetchone()[0]


cursor.execute("SELECT AVG(balance) FROM Users")
avg_balance = cursor.fetchone()[0]
print(avg_balance)


connection.commit()
connection.close()
