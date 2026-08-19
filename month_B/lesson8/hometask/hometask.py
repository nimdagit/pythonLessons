import sqlite3


def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return conn


def create_table(conn, sql_create):
    try:
        cursor = conn.cursor()
        cursor.execute(sql_create)
    except sqlite3.Error as e:
        print(e)
    return conn


def insert_contries(conn, sql_counties):
    sql_core = """INSERT INTO countries (title)
    VALUES (?)"""
    try:
        cursor = conn.cursor()
        cursor.execute(sql_core, (sql_counties,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)
    return conn


def insert_cities(conn, sql_cities):
    sql_core = """INSERT INTO cities (title, area, country_id) VALUES (
        ?,?,?
        )"""
    try:
        cursor = conn.cursor()
        cursor.execute(sql_core, sql_cities)
        conn.commit()
    except sqlite3.Error as e:
        print(e)
    return conn


def insert_students(conn, sql_students):
    sql_core = """INSERT INTO students (first_name, last_name, city_id) VALUES(
        ?,?,?
        )"""
    try:
        cursor = conn.cursor()
        cursor.execute(sql_core, sql_students)
        conn.commit()
    except sqlite3.Error as e:
        print(e)
    return conn


def select_cities(conn):
    sql_select = """SELECT id, title FROM cities"""
    try:
        cursor = conn.cursor()
        cursor.execute(sql_select)
        rows = cursor.fetchall()

        for row in rows:
            print(*list(row))
    except sqlite3.Error as e:
        print(e)
    return conn


def select_students_by_city_id(conn, user_input):
    sql_core = """SELECT s.first_name, s.last_name, country.title, city.title, city.area from cities as city
        join students as s
        on s.city_id = city.id
        join countries as country
        on country.id = city.country_id

        where city.id = ?

        """
    try:
        cursor = conn.cursor()
        cursor.execute(sql_core, (user_input,))
        rows = cursor.fetchall()

        if rows:
            for row in rows:
                print(*list(row))
        else:
            print("Ученики в выбранном городе не найдены.")
    except sqlite3.Error as e:
        print(e)
    return conn




connection = create_connection(r".\month_B\lesson8\hometask\students_and_cities.db")

if connection != None:
    sql_create_countries = """CREATE TABLE countries (
        id integer primary key autoincrement,
        title varchar(30) not null
        )"""

    create_table(connection, sql_create_countries)

    insert_contries(connection,'KYRGYZSTAN')
    insert_contries(connection,'USA')
    insert_contries(connection,'JAPAN')

    sql_create_cities = """CREATE TABLE cities (
        id integer primary key autoincrement,
        title varchar(30) not null,
        area float not null default 0,
        country_id integer references countries(id)
        )"""

    create_table(connection, sql_create_cities)

    cities = [
        ("Бишкек", 169.9, 1),
        ("Ош", 182.5, 1),
        ("Каракол", 48.0, 1),
        ("Нью-Йорк", 783.8, 2),
        ("Лос-Анджелес", 1213.9, 2),
        ("Токио", 2194.0, 3),
        ("Осака", 225.34, 3)
    ]
    for city in cities:
        insert_cities(connection, (city))


    sql_create_students = """CREATE TABLE students (
        id integer primary key autoincrement,
        first_name varchar(30) not null,
        last_name varchar(30) not null,
        city_id integer references cities(id))"""

    create_table(connection, sql_create_students)

    students = [
        ("Иван", "Петров", 1),
        ("Алексей", "Смирнов", 2),
        ("Данияр", "Ибраимов", 3),
        ("Азамат", "Токтосунов", 1),
        ("Бакыт", "Садыков", 2),
        ("Джон", "Смит", 4),
        ("Майкл", "Джонсон", 5),
        ("Эмили", "Уильямс", 4),
        ("Дэвид", "Браун", 5),
        ("Харуто", "Танака", 6),
        ("Юки", "Сато", 7),
        ("Кэнто", "Сузуки", 6),
        ("София", "Иванова", 1),
        ("Мария", "Кузнецова", 2),
        ("Такуми", "Ямамото", 7)
    ]

    for student in students:
        insert_students(connection, student)

    print("Вы можете отобразить список учеников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")
    select_cities(connection)


    while True:
        print(
            "\nВы можете отобразить список учеников по выбранному "
            "id города из перечня городов ниже, для выхода из программы "
            "введите 0:"
        )

        select_cities(connection)

        try:
            x = int(input("Введите id города: "))
        except ValueError:
            print("Введите число.")
            continue

        if x == 0:
            print("Выполняется выход...")
            break

        select_students_by_city_id(connection, x)