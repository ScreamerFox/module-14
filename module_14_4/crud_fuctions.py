import sqlite3


connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

#Создание бд____________________________________________________________________________________________________________
def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INT,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL
    );
    ''')



#Создание продукта______________________________________________________________________________________________________
def create_prod():
    cursor.execute("INSERT INTO Products(id, title, description, price) VALUES (?, ?, ?, ?)",
    (1, 'BCAA', 'Витамины BCAA', 1000))
    cursor.execute("INSERT INTO Products (id, title, description, price) VALUES (?, ?, ?, ?)",
    (2, 'домашняя еда', 'Нормальная домашняя вкуснятина', 1530))
    cursor.execute("INSERT INTO Products (id, title, description, price) VALUES (?, ?, ?, ?)",
    (3, 'ANABOL', 'Анаболики', 3000))
    cursor.execute("INSERT INTO Products (id, title, description, price) VALUES (?, ?, ?, ?)",
    (4, 'Сет спортивного питания', 'Несколько видов BCAA, протеин, креатин', 5000))
    connection.commit()


def get_all_products():
    cursor.execute('SELECT * FROM Products')
    return cursor.fetchall()

def create_4_prod():
    if not get_all_products():
        create_prod()


def add_prod(id, title, description, price):
    cursor.execute("INSERT INTO Products(id, title, description, price) VALUES (?,?,?,?)", (id, title, description, price))



if __name__ == '__main__':
    initiate_db()
    create_4_prod()
    connection.commit()




