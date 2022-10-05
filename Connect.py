import mysql.connector
from mysql.connector import Error


class Connect:

    def __init__(self):
        pass

    @staticmethod
    def connect():
        co = mysql.connector.connect(host='localhost',
                                     database='enigmapy',
                                     user='admin',
                                     password='admin')
        print('MySQL co is open')
        return co

    @staticmethod
    def run(co, query):
        curs = co.cursor()
        res = curs.execute(query)
        result = curs.fetchall()
        co.commit()
        return result

    @staticmethod
    def close(co):
        # fermer la connection
        co.close()
        print("MySQL co is closed")
