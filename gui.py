import sys
import logging

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication, QDialog

import facade
from facade import Facade

from PyQt5 import uic, QtWidgets
from PyQt5.Qt import *

logging.basicConfig(level=logging.INFO)


class AuthWindow(QDialog):
    def __init__(self, parent=None):
        super(AuthWindow, self).__init__(parent)
        self.auth_log = ''
        self.ui = uic.loadUi("forms/auth.ui", self)
        self.setWindowTitle("Авторизация")
        self.setWindowIcon(QIcon('res/shar.png'))
        self.facade = Facade()
        self.ui.btn_exit.clicked.connect(self.exit)
        self.ui.btn_enter.clicked.connect(self.enter)
        self.log_for = ''

    def mes_box(self, text):
        """
        Открывает messagebox с переданным текстом.
        Вызывается при неверном вводе пользователем логина, пароля, капчи.
        :param text: текст для вывода в messagebox
        """
        self.messagebox = QMessageBox(self)
        self.messagebox.setWindowTitle("Ошибка")
        self.messagebox.setText(text)
        self.messagebox.setStandardButtons(QMessageBox.Ok)
        self.messagebox.show()
        log_for = ''

    def exit(self):
        self.hide()
        self.open_auth()

    def enter(self):
        self.auth_log = self.ui.line_login.text()
        auth_pas = self.ui.line_password.text()

        if self.auth_log == '' or auth_pas == '':
            logging.log(logging.INFO, 'Ошибка. Заполните все поля!')
            self.mes_box('Заполните все поля!')
        else:
            password, role = self.facade.get_for_authorization(self.auth_log)

            if password != auth_pas:
                logging.log(logging.INFO, 'Ошибка. Неправильно введены данные.')
                self.mes_box('Неправильно введены данные.')
            elif password == auth_pas:
                logging.log(logging.INFO, 'Вход выполнен')
                log_for = self.auth_log
                if role == 'Клиент':
                    self.close()
                    self.ui = MainWindow()
                    self.ui.show()
                else:   # Admin
                    self.close()
                    self.ui = AdminWindow()
                    self.ui.show()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("forms/main.ui", self)
        self.setWindowTitle("Главная")
        self.setWindowIcon(QIcon('res/shar.png'))
        self.ui.btn_exit.clicked.connect(self.exit)
        self.ui.btn_profile.clicked.connect(self.profile)
        self.ui.btn_search.clicked.connect(self.search)

    def exit(self):
        self.close()
        self.ui = AuthWindow()
        self.ui.show()

    def open_auth(self):
        dialog = AuthWindow(self)
        dialog.setWindowTitle("Авторизация")
        dialog.show()

    def profile(self):
        self.ui = ProfileWindow()
        self.ui.show()

    def search(self):
        self.ui = SearchWindow()
        self.ui.show()


class ProfileWindow(QMainWindow):
    def __init__(self, parent=None):
        super(ProfileWindow, self).__init__(parent)
        self.ui = uic.loadUi("forms/profile.ui", self)
        self.facade = Facade()
        self.setWindowTitle("Моя анкета")
        self.setWindowIcon(QIcon('res/shar.png'))
        self.ui.btn_edit.clicked.connect(self.edit)
        self.ui.btn_exit.clicked.connect(self.exit)
        self.auth = AuthWindow()

        self.info = self.facade.get_client_info(self.auth.log_for)
        self.ui.label_name = self.info[0]
        self.ui.label_sex = self.info[1]
        self.ui.label_age = self.info[2]
        self.ui.label_height = self.info[3]
        self.ui.label_weight = self.info[4]
        self.ui.label_zodiac = self.info[5]
        self.ui.label_eyes = self.info[6]
        self.ui.label_hair = self.info[7]
        self.ui.label_phone = self.info[8]

    def edit(self):
        self.ui = EditWindow()
        self.ui.show()

    def exit(self):
        self.close()


class EditWindow(QMainWindow):
    def __init__(self):
        super(EditWindow, self).__init__()
        self.ui = uic.loadUi("forms/edit.ui", self)
        self.setWindowTitle("Редактирование анкеты")
        self.setWindowIcon(QIcon('res/shar.png'))


class SearchWindow(QMainWindow):
    def __init__(self):
        super(SearchWindow, self).__init__()
        self.ui = uic.loadUi("forms/search.ui", self)
        self.setWindowTitle("Поиск пары")
        self.setWindowIcon(QIcon('res/shar.png'))


class AdminWindow(QMainWindow):
    def __init__(self):
        super(AdminWindow, self).__init__()
        self.ui = uic.loadUi("forms/admin.ui", self)
        self.setWindowTitle("Администратор")
        self.setWindowIcon(QIcon('res/shar.png'))
        self.ui.btn_exit.clicked.connect(self.exit)
        self.ui.btn_clients.clicked.connect(self.clients)
        self.ui.btn_users.clicked.connect(self.users)
        self.ui.btn_zodiacs.clicked.connect(self.zodiacs)
        self.ui.btn_hairs.clicked.connect(self.hairs)
        self.ui.btn_eyes.clicked.connect(self.eyes)

    def exit(self):
        self.close()
        self.ui = AuthWindow()
        self.ui.show()

    def clients(self):
        self.ui = ClientWindow()
        self.ui.show()

    def users(self):
        self.ui = UserWindow()
        self.ui.show()

    def zodiacs(self):
        self.ui = ZodiacWindow()
        self.ui.show()

    def hairs(self):
        self.ui = HairWindow()
        self.ui.show()

    def eyes(self):
        self.ui = EyeWindow()
        self.ui.show()


class ClientWindow(QMainWindow):
    def __init__(self):
        super(ClientWindow, self).__init__()
        self.ui = uic.loadUi("forms/clients.ui", self)
        self.setWindowTitle("Просмотр клиентов")
        self.setWindowIcon(QIcon('res/shar.png'))
        self.facade = Facade()
        self.table = self.ui.table_clients
        self.cout_client()
        self.ui.btn_exit.clicked.connect(self.exit)

    def cout_client(self):
        self.table.clear()
        rec = self.facade.read_clients()
        self.table.setColumnCount(11)  # кол-во столбцов
        self.table.setRowCount(len(rec))  # кол-во строк
        self.table.setHorizontalHeaderLabels(['Код клиента', 'ФИО', 'Пол', 'Возраст', 'Рост', 'Вес', 'Статус', 'Код знака', 'Код глаз', 'Код волос', 'Телефон'])  # название колонок таблицы

        for i, client in enumerate(rec):
            for x, field in enumerate(client):  # i, x - координаты ячейки, в которую будем записывать текст
                item = QTableWidgetItem()
                item.setText(str(field))  # записываем текст в ячейку
                if x == 0:  # для id делаем некликабельные ячейки
                    item.setFlags(Qt.ItemIsEnabled)
                self.table.setItem(i, x, item)

    def exit(self):
        self.close()


class UserWindow(QMainWindow):
    def __init__(self):
        super(UserWindow, self).__init__()
        self.ui = uic.loadUi("forms/clients.ui", self)
        self.setWindowTitle("Просмотр пользователей")
        self.setWindowIcon(QIcon('res/shar.png'))
        self.facade = Facade()
        self.table = self.ui.table_clients
        self.cout_client()
        self.ui.btn_exit.clicked.connect(self.exit)

    def cout_client(self):
        self.table.clear()
        rec = self.facade.read_users()
        self.table.setColumnCount(5)  # кол-во столбцов
        self.table.setRowCount(len(rec))  # кол-во строк
        self.table.setHorizontalHeaderLabels(['Код пользователя', 'Роль', 'Логин', 'Пароль', 'Код клиента'])  # название колонок таблицы

        for i, client in enumerate(rec):
            for x, field in enumerate(client):  # i, x - координаты ячейки, в которую будем записывать текст
                item = QTableWidgetItem()
                item.setText(str(field))  # записываем текст в ячейку
                if x == 0:  # для id делаем некликабельные ячейки
                    item.setFlags(Qt.ItemIsEnabled)
                self.table.setItem(i, x, item)

    def exit(self):
        self.close()


class ZodiacWindow(QMainWindow):
    def __init__(self):
        super(ZodiacWindow, self).__init__()
        self.ui = uic.loadUi("forms/clients.ui", self)
        self.setWindowTitle("Просмотр знаков зодиака")
        self.setWindowIcon(QIcon('res/shar.png'))
        self.facade = Facade()
        self.table = self.ui.table_clients
        self.cout_client()
        self.ui.btn_exit.clicked.connect(self.exit)

    def cout_client(self):
        self.table.clear()
        rec = self.facade.read_zodiacs()
        self.table.setColumnCount(3)  # кол-во столбцов
        self.table.setRowCount(len(rec))  # кол-во строк
        self.table.setHorizontalHeaderLabels(['Код знака', 'Название', 'Описание'])  # название колонок таблицы

        for i, client in enumerate(rec):
            for x, field in enumerate(client):  # i, x - координаты ячейки, в которую будем записывать текст
                item = QTableWidgetItem()
                item.setText(str(field))  # записываем текст в ячейку
                if x == 0:  # для id делаем некликабельные ячейки
                    item.setFlags(Qt.ItemIsEnabled)
                self.table.setItem(i, x, item)

    def exit(self):
        self.close()


class HairWindow(QMainWindow):
    def __init__(self):
        super(HairWindow, self).__init__()
        self.ui = uic.loadUi("forms/clients.ui", self)
        self.setWindowTitle("Просмотр цветов волос")
        self.setWindowIcon(QIcon('res/shar.png'))
        self.facade = Facade()
        self.table = self.ui.table_clients
        self.cout_client()
        self.ui.btn_exit.clicked.connect(self.exit)

    def cout_client(self):
        self.table.clear()
        rec = self.facade.read_hairs()
        self.table.setColumnCount(2)  # кол-во столбцов
        self.table.setRowCount(len(rec))  # кол-во строк
        self.table.setHorizontalHeaderLabels(['Код волос', 'Название'])  # название колонок таблицы

        for i, client in enumerate(rec):
            for x, field in enumerate(client):  # i, x - координаты ячейки, в которую будем записывать текст
                item = QTableWidgetItem()
                item.setText(str(field))  # записываем текст в ячейку
                if x == 0:  # для id делаем некликабельные ячейки
                    item.setFlags(Qt.ItemIsEnabled)
                self.table.setItem(i, x, item)

    def exit(self):
        self.close()


class EyeWindow(QMainWindow):
    def __init__(self):
        super(EyeWindow, self).__init__()
        self.ui = uic.loadUi("forms/clients.ui", self)
        self.setWindowTitle("Просмотр цветов глаз")
        self.setWindowIcon(QIcon('res/shar.png'))
        self.facade = Facade()
        self.table = self.ui.table_clients
        self.cout_client()
        self.ui.btn_exit.clicked.connect(self.exit)

    def cout_client(self):
        self.table.clear()
        rec = self.facade.read_eyes()
        self.table.setColumnCount(2)  # кол-во столбцов
        self.table.setRowCount(len(rec))  # кол-во строк
        self.table.setHorizontalHeaderLabels(['Код глаз', 'Название'])  # название колонок таблицы

        for i, client in enumerate(rec):
            for x, field in enumerate(client):  # i, x - координаты ячейки, в которую будем записывать текст
                item = QTableWidgetItem()
                item.setText(str(field))  # записываем текст в ячейку
                if x == 0:  # для id делаем некликабельные ячейки
                    item.setFlags(Qt.ItemIsEnabled)
                self.table.setItem(i, x, item)

    def exit(self):
        self.close()


class Builder:
    def __init__(self):
        self.qapp = QApplication(sys.argv)
        self.window = MainWindow()
        self.auth()

    def auth(self):
        self.window.open_auth()
        self.qapp.exec()


if __name__ == '__main__':
    B = Builder()