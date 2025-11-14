import random
import sqlite3
from sqlite3 import Error
from pathlib import Path
from faker import Faker


db_file_path = Path(__file__).parent / "first_db.db"


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
        return cursor
    except Error as e:
        print(f"The error '{e}' occurred")


def read_query(connection, query):
    try:
        cursor = execute_query(connection, query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


conn = create_connection(db_file_path)
print(conn)


create_users_table = """
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  age INTEGER,
  gender TEXT,
  nationality TEXT
);
"""
make_table = execute_query(conn, create_users_table)

create_posts_table = """
CREATE TABLE IF NOT EXISTS posts(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  description TEXT NOT NULL,
  user_id INTEGER NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users (id)
);
"""
create_comments_table = """
CREATE TABLE IF NOT EXISTS comments (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  text TEXT NOT NULL,
  user_id INTEGER NOT NULL,
  post_id INTEGER NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users (id) FOREIGN KEY (post_id) REFERENCES posts (id)
);
"""

create_likes_table = """
CREATE TABLE IF NOT EXISTS likes (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  post_id integer NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users (id) FOREIGN KEY (post_id) REFERENCES posts (id)
);
"""

create_emails_table = """
CREATE TABLE IF NOT EXISTS emails (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    email TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id)
);
"""
# create_all = [create_posts_table, create_comments_table, create_likes_table, create_emails_table]
# for q in create_all:
#     execute_query(conn, q)


fake = Faker("uk_UA")

def user_gen() -> str:
    genger = "female" if random.choice((True, False)) else "male"
    name = fake.name_male() if genger == "male" else fake.name_female()
    age = random.randint(10, 90)
    nationality = fake.region()
    yield name, age, genger, nationality

def users_creation():
    users_list = []
    for _ in range(300):
        user = next(user_gen())
        users_list.append(user)
    #print(users_list)

    insert_users = f"""
        INSERT INTO
            users (name, age, gender, nationality)
        VALUES
        """
    final_insert = ""
    for user in users_list:
        final_insert = final_insert + f"('{user[0]}', '{user[1]}', '{user[2]}', '{user[3]}'),"
    execute_query(conn, insert_users + final_insert[:-1])
    # Варіант повільного виконання
    # for user in users_list:
    #     final_insert = insert_users + f"('{user[0]}', '{user[1]}', '{user[2]}', '{user[3]}');"
    #     execute_query(conn, final_insert)

select_users = "SELECT * from users"
users = read_query(conn, select_users)

for user in users:
    print(user)

where_query = """
SELECT id, name, age
FROM users
WHERE age > 40;
"""
users = read_query(conn, where_query)
print(len(users))

in_not_in_query = """
SELECT id, name
FROM users
WHERE nationality IN ('Чернівецька область', 'Чернігівська область', 'Чад');
"""
users = read_query(conn, in_not_in_query)
print(users)
