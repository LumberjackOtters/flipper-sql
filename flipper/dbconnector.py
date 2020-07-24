import mysql.connector
from mysql.connector import Error
import pprint

def connect(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("Connection to MySQL DB successful")
    except Error as error:
        pprint.pprint(error)

    return connection

def execute_query(connection, query):
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as error:
        pprint.pprint(error)

def execute_many_query(connection, query, values):
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.executemany(query, values)
        connection.commit()
    except Error as error:
        pprint.pprint(error)


def execute_read_query(connection, query):
    cursor = connection.cursor(dictionary=True)
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as error:
        pprint.pprint(error)
