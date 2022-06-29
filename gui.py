import sys
import logging

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication, QDialog

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


class ProfileWindow(QDialog):
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