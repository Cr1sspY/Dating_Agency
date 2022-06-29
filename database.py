import mysql
from mysql.connector import connect


class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(host='localhost', port=3306, user='root', password='12345', database='dating_agency')

    def get_info(self, login):
        log = []
        cursor = self.conn.cursor()
        cursor.execute(
            f"""SELECT Пароль, Роль FROM пользователи WHERE Логин = '{login}'""")
        rows = cursor.fetchall()
        for i in rows:
            for j in i:
                log.append(j)
        return log
        cursor.close()

    def get_logins(self):
        logins = []
        cursor = self.conn.cursor()
        cursor.execute(f"""SELECT Логин FROM пользователи""")
        rows = cursor.fetchall()

        for i in rows:
            for j in i:
                logins.append(j)
        return logins
        cursor.close()

    def get_client_info(self, login):
        client = []
        cursor = self.conn.cursor()
        cursor.execute(f"""SELECT Код_Клиента FROM пользователи WHERE Логин='{login}'""")
        code = cursor.fetchone()
        cursor.execute(f"""SELECT ФИО, Пол, Возраст, рост, вес, статус, Код_Знака, Код_Глаз, Код_Волос FROM клиенты WHERE Код_клиента='{code}'""")
        rows = cursor.fetchall()
        for i in rows:
            for j in i:
                client.append(j)
        return client
        cursor.close()

    def get_other_client_info(self, login):
        oth_client = []
        cursor = self.conn.cursor()
        cursor.execute(f"""SELECT Код_Клиента FROM пользователи WHERE Логин!='{login}'""")
        code = cursor.fetchone()
        cursor.execute(f"""SELECT ФИО, Пол, Возраст, рост, вес, статус, Код_Знака, Код_Глаз, Код_Волос FROM клиенты WHERE Код_клиента='{code}'""")
        rows = cursor.fetchall()
        for i in rows:
            for j in i:
                oth_client.append(j)
        return oth_client
        cursor.close()
