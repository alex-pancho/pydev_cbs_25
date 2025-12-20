from psycopg2 import connect
from psycopg2 import OperationalError


def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = connect(
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


def execute_query(connection, query:str, return_data:bool=True):
    connection.autocommit = True
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        print("Query executed successfully")
        if return_data:
            result = cursor.fetchall()
            return result
    except OperationalError as e:
        print(f"The error '{e}' occurred")


def conn_params():
    win = False

    if win:
        database = "norwind"
        user = "postgres"
        password = "pan"
        host = "127.0.0.1"
        port = 5433
    else:
        host = "172.24.215.31"  # ВАЖЛИВО $ ip addr show eth0
        port = 5432
        database = "sql_essential_db"
        user = "student"
        password = "pan"

    connection = create_connection(
        db_name=database, db_user=user, db_password=password, db_host=host, db_port=port
    )
    return connection

query = """
SELECT *
FROM customers;
"""

query_2 = """
SELECT COUNT(*)
FROM customers;
"""

query_result = execute_query(
    connection=conn_params(),
    query=query
)

print(query_result)
#print(len(query_result))

query_result = execute_query(
    connection=conn_params(),
    query=query_2
)

print(query_result)

orders_some_attributes_sample = """
SELECT order_id, order_date, shipped_date, ship_city
FROM orders
where order_id beetwen 5000
"""
query_result = execute_query(
    connection=conn_params(),
    query=orders_some_attributes_sample
)

print(query_result)