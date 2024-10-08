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
    cursor.execute('''
    INSERT INTO Users (id, username, email, age, balance) VALUES (?, ?, ?, ?, ?)
    ''', (f'{i+1}', f'User{i}', f'example{i}@gmail.com', f'{(i+1) * 10}', 1000))


cursor.execute("SELECT * FROM Users")
rows = list(cursor.fetchall())


for row in rows[::2]:
    cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", (500, row[0],))


for row in rows[::3]:
    cursor.execute("DELETE FROM Users WHERE id = ?", (row[0],))


cursor.execute("SELECT * FROM Users WHERE age != ?", (60,))
row_age = list(cursor.fetchall())

connection.commit()
connection.close()


for i in row_age:
    print(f'Имя - {i[1]}, Почта - {i[2]}, Возраст - {i[3]}, Баланс - {i[4]}')
