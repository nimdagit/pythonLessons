import sqlite3


# 1. Создать базу данных hw.db в sqlite через код python, используя модуль sqlite3
# 2. В БД создать таблицу products
# 4. Добавить поле product_title текстового типа данных максимальной длиной 200 символов, поле не должно быть пустым (NOT NULL)
# 5. Добавить поле price не целочисленного типа данных размером 10 цифр из которых 2 цифры после плавающей точки, поле не должно быть пустым (NOT NULL) значением по-умолчанию поля должно быть 0.0
# 6. Добавить поле quantity целочисленного типа данных, поле не должно быть пустым (NOT NULL) значением по-умолчанию поля должно быть 0
# 7. Добавить функцию, которая бы добавляла в БД 15 различных товаров
# 8. Добавить функцию, которая меняет количество товара по id
# 9. Добавить функцию, которая меняет цену товара по id
# 10. Добавить функцию, которая удаляет товар по id
# 11. Добавить функцию, которая бы выбирала все товары из БД и распечатывала бы их в консоли
# 12. Добавить функцию, которая бы выбирала из БД товары, которые дешевле лимита (100 сом) сомов и количество которых больше чем лимит остатка на складе (5 шт) и распечатывала бы их в консоли
# 13. Добавить функцию, которая бы искала в БД товары по названию (Например: искомое слово “мыло”, должны соответствовать поиску товары с названием - “Жидкое мыло с запахом ванили”, “Мыло детское” и тд.)
# 14. Протестировать каждую написанную функцию


def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        
    except sqlite3.Error as e:
        print(e)
    return conn


def insert_tuple(conn, sql_values):
    sql_core ="""INSERT INTO products (product_title, price, quantity)
    VALUES(?, ?, ?)
    """
    try:
        cursor = conn.cursor()
        for sql_one_tuple in sql_values:
            cursor.execute(sql_core, sql_one_tuple)

        conn.commit()
    except sqlite3.Error as e:
        print(e)
    return conn


def update_quantity(conn, setvalue_and_idnum):
    sql_core = """UPDATE products SET quantity = ?
    WHERE id = ?"""
    try:
        cursor = conn.cursor()
        cursor.execute(sql_core, setvalue_and_idnum)
        conn.commit()
    except sqlite3.Error as e:
        print(e)
    return conn

def update_price(conn, setvalue_and_idnum):
    sql_core = """UPDATE products SET price = ?
    WHERE id = ?"""
    try:
        cursor = conn.cursor()
        cursor.execute(sql_core, setvalue_and_idnum)
        conn.commit()
    except sqlite3.Error as e:
        print(e)
    return conn

def delete_product(conn, idnum):
    sql_core = """DELETE from products WHERE id = ?"""
    try:
        cursor = conn.cursor()
        cursor.execute(sql_core, (idnum,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)
    return conn

def select_all_products(conn):
    sql = """SELECT * FROM products"""
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        rows_list = cursor.fetchall()

        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)
    return conn

def select_by_filters(conn, filter_parametrs):
    sql_core = """SELECT * FROM products
    WHERE price < ? AND quantity > ?"""
    try:
        cursor = conn.cursor()
        cursor.execute(sql_core, filter_parametrs)
        rows_list = cursor.fetchall()

        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)
    return conn

def select_by_name(conn, product_title):
    sql_core ="""SELECT * FROM products
    WHERE product_title like ?
    """
    try:
        cursor = conn.cursor()
        cursor.execute(sql_core, ('%' + product_title + '%',))
        rows_list = cursor.fetchall()

        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)
    return conn

connection = create_connection(r".\month_B\lesson7\hometask\hw.db")
if connection != None:
    print('Successfully connected to DB!')

    create_table_sql =""" CREATE TABLE products(
    id integer primary key autoincrement,
    product_title varchar(200) not null,
    price numeric(10, 2) not null default 0.0,
    quantity integer not null default 0
    )"""

    create_table(connection, create_table_sql)

    products = [
    ("Milk", 85.85, 20),
    ("Bread", 45.50, 35),
    ("Butter", 120.00, 15),
    ("Cheese", 250.00, 12),
    ("Eggs", 110.00, 30),
    ("Chicken", 280.00, 18),
    ("Beef", 450.00, 10),
    ("Rice", 95.00, 25),
    ("Pasta", 75.00, 30),
    ("Sugar", 80.00, 22),
    ("Salt", 35.00, 40),
    ("Flour", 70.00, 28),
    ("Apple Juice", 130.00, 16),
    ("Orange Juice", 150.00, 14),
    ("Chocolate", 100.00, 20),
]
    insert_tuple(connection, products)

    update_quantity(connection, (15, 15))
    update_price(connection, (120, 15))

    delete_product(connection, 8)

    print('все товары')
    select_all_products(connection)
    print('товары по фильтрам')
    select_by_filters(connection, (100, 5))
    print('товары по совпадению имени')
    select_by_name(connection, 'JUI')
