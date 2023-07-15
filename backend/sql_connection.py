import mysql.connector
__con=None
def get_sql_connection():
    global __con
    if __con is None:
        __con=mysql.connector.connect(host="localhost",user="root",passwd="",database="grocery_store")
    return __con