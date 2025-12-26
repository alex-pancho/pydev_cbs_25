import time
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
        #print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


def execute_query(connection, query:str, return_data:bool=True):
    connection.autocommit = True
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        #print("Query executed successfully")
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
        host = "172.30.6.182"  # ВАЖЛИВО $ ip addr show eth0
        port = 5432
        database = "sql_essential_db"
        user = "student"
        password = "pan"

    connection = create_connection(
        db_name=database, db_user=user, db_password=password, db_host=host, db_port=port
    )
    return connection

connection = conn_params()

# query = """
# SELECT *
# FROM customers;
# """

# query_2 = """
# SELECT COUNT(*)
# FROM customers;
# """
# 

# query_result = execute_query(
#     connection=connection,
#     query=query
# )

# #print(query_result)
# ##print(len(query_result))

# query_result = execute_query(
#     connection=connection,
#     query=query_2
# )

# #print(query_result)

# orders_some_attributes_sample = """
# SELECT order_id, order_date, shipped_date, ship_city
# FROM orders
# where order_id between 11015 and 11056
# order by order_id
# """
# query_result = execute_query(
#     connection=connection,
#     query=orders_some_attributes_sample
# )

# #print(query_result)





# operation_query_d = """
# SELECT DISTINCT country
# FROM customers;
# """


# operation_query_g = """
# SELECT country
# FROM customers
# GROUP BY country;
# """
def timestat(operation_query, method="", prn=False):
    start = time.time()
    query_result = execute_query(
        connection=connection,
        query=operation_query,
        return_data=prn
    )
    if prn: print(query_result, f"\nLEN: {len(query_result)}")

    end = time.time()
    print(f"Час виконання {method}: {end - start:.6f} сек")

# timestat(operation_query_d, method="DISTINCT")
# timestat(operation_query_g, method="GROUP BY")
# operation_query_candy = """
# SELECT DISTINCT COUNT(country)
# FROM employees;
# """
# operation_query_gry = """
# SELECT COUNT(country), country
# FROM employees
# GROUP BY country;
# """
# timestat(operation_query_d, method="COUNTDISTINCT", prn=True)#
# timestat(operation_query_gry, method="GROUP BY ", prn=True)

# operation_query = """
# SELECT COUNT(country), country
# FROM suppliers
# GROUP BY country;
# """
# timestat(operation_query, method="GROUP BY", prn=True)
# operation_query_dd = """
# SELECT COUNT(DISTINCT country)
# FROM suppliers
# ;
# """
# timestat(operation_query_dd, method="DISINCT", prn=True)

# operation_query = """
# SELECT company_name, city, phone, country
# FROM suppliers
# WHERE country IN ('USA','Germany');
# """
# timestat(operation_query, method="=>", prn=True)

# operation_query = """
# SELECT *
# FROM orders
# INNER JOIN shippers ON orders.ship_via = shippers.shipper_id
# WHERE orders.customer_id = 'WARTH';
# """

# timestat(operation_query, method="INNER JOIN", prn=True)

# operation_query = """
# SELECT orders.order_date, orders.order_id, products.product_name, order_details.unit_price, order_details.discount, order_details.quantity, ( order_details.unit_price * (1 - order_details.discount) * order_details.quantity) AS total_price, orders.ship_country
# FROM orders
# INNER JOIN order_details ON orders.order_id = order_details.order_id
# INNER JOIN products ON products.product_id = order_details.product_id;
# """
# timestat(operation_query, method="2xINNER", prn=True)

operation_query = """
SELECT customers.customer_id, customers.company_name, orders.order_id
FROM customers
LEFT JOIN orders ON  customers.customer_id = orders.customer_id
WHERE orders.order_id IS NULL;
"""
operation_query = """
SELECT customers.customer_id, customers.company_name, COUNT(*) as cnt
FROM customers
LEFT JOIN orders ON  customers.customer_id = orders.customer_id
group by customers.customer_id
having COUNT(*) > 5
"""

operation_query = """
SELECT company_name, contact_name, contact_title, city
FROM suppliers
WHERE city in (
    SELECT DISTINCT city
    FROM employees
    );
"""
op_query = """
SELECT distinct customer_id
    FROM orders
    JOIN order_details USING(order_id)
    WHERE quantity > 50
"""
timestat(op_query, method="sub select", prn=True)

operation_query = f"""
SELECT company_name, contact_name, contact_title
FROM customers
WHERE customer_id = ANY(
    {op_query}
);
"""
# timestat(operation_query, method="sub select", prn=True)

operation_query = """
CREATE OR REPLACE VIEW customer_orders AS 
SELECT orders.order_id, orders.customer_id, orders.order_date 
FROM orders;
"""
timestat(operation_query, method="VIEW")
operation_query = """
SELECT * 
FROM customer_orders;
"""
timestat(operation_query, method="sub select", prn=True)