import sqlite3



connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INT,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL
    );
    ''')

def get_all_products():
    cursor.execute('SELECT * FROM Products')
    return cursor.fetchall()

initiate_db()

cursor.execute("INSERT INTO Products (id, title, description, price) VALUES (?, ?, ?, ?)",
(1, 'BCAA', 'Витамины BCAA', 1000))
cursor.execute("INSERT INTO Products (id, title, description, price) VALUES (?, ?, ?, ?)",
    (2, 'домашняя еда', 'Нормальная домашняя вкуснятина', 1530))
cursor.execute("INSERT INTO Products (id, title, description, price) VALUES (?, ?, ?, ?)",
    (3, 'ANABOL', 'Анаболики', 3000))
cursor.execute("INSERT INTO Products (id, title, description, price) VALUES (?, ?, ?, ?)",
    (4, 'Сет спортивного питания', 'Несколько видов BCAA, протеин, креатин', 5000))





connection.commit()

