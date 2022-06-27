import sys
import logging

from facade import Facade

from PyQt5 import uic, QtWidgets
from PyQt5.Qt import *

logging.basicConfig(level=logging.INFO)


class AuthWindow(QMainWindow):
    def __init__(self):
        super(AuthWindow, self).__init__()
        self.ui = uic.loadUi("forms/auth.ui", self)
        self.setWindowTitle("Авторизация")
        self.setWindowIcon(QIcon('res/shar.png'))
        self.facade = Facade()
        self.ui.btn_exit.clicked.connect(self.exit)
        self.ui.btn_enter.clicked.connect(self.enter)

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

    def exit(self):
        self.close()
        sys.exit(app.exec_())

    def enter(self):
        auth_log = self.ui.line_login.text()
        auth_pas = self.ui.line_password.text()

        if auth_log == '' or auth_pas == '':
            logging.log(logging.INFO, 'Ошибка. Заполните все поля!')
            self.mes_box('Заполните все поля!')
        else:
            password, role = self.parent().facade.get_for_authorization(auth_log)

            if password != auth_pas:
                logging.log(logging.INFO, 'Ошибка. Неправильно введены данные.')
                self.mes_box('Неправильно введены данные.')
            elif password == auth_pas:
                logging.log(logging.INFO, 'Вход выполнен')
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
        super(MainWindow, self).__init__()
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

    def profile(self):
        self.ui = ProfileWindow()
        self.ui.show()

    def search(self):
        self.ui = SearchWindow()
        self.ui.show()


class ProfileWindow(QMainWindow):
    def __init__(self):
        super(ProfileWindow, self).__init__()
        self.ui = uic.loadUi("forms/profile.ui", self)
        self.setWindowTitle("Моя анкета")
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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = AuthWindow()
    window.show()
    sys.exit(app.exec_())