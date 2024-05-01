import mysql.connector
from getpass import getpass
from mysql.connector import connect, Error

def show_all():
    show_table_query = "SELECT * FROM movies"
    with connection.cursor() as cursor:
        cursor.execute(show_table_query)
        result = cursor.fetchall()
        for row in result:
            session_time_str = str(row[3])
            print(row[0], row[1], row[2], session_time_str)
        print('\n')
        

def update(column, column_value, where):
    update_query = """
            UPDATE
                movies
            SET
                {} = %s
            WHERE
                id = %s
            """.format(column)
    with connection.cursor() as cursor:
        cursor.execute(update_query, (column_value, where))
        connection.commit()

def add(title, hall, session):
    insert_query = """
            INSERT INTO movies (title, hall, session)
            VALUES (%s, %s, %s)
            """
    with connection.cursor() as cursor:
        cursor.execute(insert_query, (title, hall, session))
        connection.commit()

def delete_movie(movie_id):
    delete_query = """
            DELETE FROM movies
            WHERE id = %s
            """
    with connection.cursor() as cursor:
        cursor.execute(delete_query, (movie_id,))
        connection.commit()
    
    update_id_query = """
            ALTER TABLE movies AUTO_INCREMENT = 1
            """
    with connection.cursor() as cursor:
        cursor.execute(update_id_query)
        connection.commit()

try:
    with connect(
        host="localhost",
        user='root',
        password='528406',
        database="cinema",
    ) as connection:
        inp = ""
        while inp != "0":
            print("1. Посмотреть \n2. Добавить \n3. Изменить \n4. Удалить")
            inp = input("Введите цифру: ")
            print("\n")

            match inp:
                case "1":
                    show_all()
                case "2":
                    title = input("Название: ")
                    hall = input("Зал: ")
                    session = input("Сеанс(чч:мм:сс): ")
                    add(title, hall, session)
                case "3":
                    id = input("Какой фильм вы хотите изменить? Введите id: ")
                    inp1 = input("Что вы хотите изменить? \n1. Название\n2. Холл\n3. Сеанс\n4. Все/n Номер: ")           
                    match inp1:
                        case "1":
                            new_title = input("Новое название: ")
                            update("title", new_title, id)
                        case "2":
                            new_hall = input("Новое зал: ")
                            update("hall", new_hall, id)
                        case "3":
                            new_session = input("Новый сеанс: ")
                            update("session", new_session, id)
                        case "4":
                            new_title = input("Новое название: ")
                            new_hall = input("Новое холл: ")
                            new_session = input("Новый сеанс: ")
                            update("title", new_title, id)
                            update("hall", new_hall, id)
                            update("session", new_session, id)
                case "4":
                    id = input("Какой фильм вы хотите удалить? Введите id: ")
                    delete_movie(id)


except Error as e:
    print(e)