import sqlite3


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

def insert_employee(conn, employee):
    sql = """INSERT INTO employees (full_name, salary, hobby, birth_date, is_married) 
    VALUES  (?, ?, ?, ?, ?)
    """
    try:
        cursor = conn.cursor()
        cursor.execute(sql, employee)
        conn.commit()
    except sqlite3.Error as e:
        print(e)
    return conn

def update_employee(conn, employee):
    sql = """UPDATE employees SET salary = ?, is_married = ?
    WHERE id = ?
    """
    try:
        cursor = conn.cursor()
        cursor.execute(sql, employee)
        conn.commit()
    except sqlite3.Error as e:
        print(e)
    return conn

def delete_employee(conn, id):
    sql = """DELETE FROM employees WHERE id = ?
    """
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)
    return conn


def select_all_employees(conn):
    sql = """SELECT * FROM employees"""
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        rows_list = cursor.fetchall()

        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)
    return conn

def select_employees_by_salary(conn, salary_limit):
    sql = """SELECT * FROM employees WHERE salary >= ?"""
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (salary_limit,))
        rows_list = cursor.fetchall()

        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)
    return conn


# sql_to_create_employees_table = """
# CREATE TABLE employees(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     full_name VARCHAR(200) NOT NULL, 
#     salary FLOAT NOT NULL DEFAULT 0.0,
#     hobby TEXT DEFAULT NULL,
#     birth_date DATE NOT NULL,
#     is_married BOOLEAN DEFAULT FALSE
# )
# """

connection = create_connection(r".\month_B\lesson7\group_ib_1-24.db")
if connection !=None:
    print('Successfully connected to DB!')
    # create_table(connection, sql_to_create_employees_table)    


    # insert_employee(connection, ('Jeffry Epstein', 1000, 'Programming', '2006-01-12', True))
    # insert_employee(connection, ('Adolf Gitler', 2000, 'Evening bonfire', '2006-01-12', True))
    # insert_employee(connection, ('Michael Jackson', 10000, 'Dancing', '2006-01-12', False))
    # insert_employee(connection, ('Cristianu ronaldo', 100000, 'Be THE BEST', '1985-02-05', False))
    # insert_employee(connection, ('Janna Dark', 1000, 'Find the Freedom', '2003-01-31', True))
    # insert_employee(connection, ('Netanyahu Benjamin', 1000, 'play with fate', '2001-04-12', False))
    # insert_employee(connection, ('Maratbek Diyazbek', 100, 'Dichkicking', '2006-11-02', True))
    # update_employee(connection, (1555, False, 2))
    delete_employee(connection, 5)

select_all_employees(connection)
select_employees_by_salary(connection, 2300)


connection.close()  