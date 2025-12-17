import psycopg2
from psycopg2 import OperationalError


def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


win = False

if win:
    database = "norwind"
    user = "postgres"
    password = "pan"
    host = "127.0.0.1"
    port = 5433
else:
    host = "172.19.237.97"  # ВАЖЛИВО $ ip addr show eth0
    port = 5432
    database = "sql_essential_db"
    user = "student"
    password = "pan"

connection = create_connection(
    db_name=database, db_user=user, db_password=password, db_host=host, db_port=port
)
