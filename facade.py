from database import Database


class Facade:
    def __init__(self):
        self.db = Database()

    def get_logins(self):
        return self.db.get_logins()

    def get_for_authorization(self, login):
        log = self.db.get_info(login)
        if not log:
            return '', ''
        password, role = log[0], log[1]  # временные данные
        return password, role

    def get_client_info(self, login):
        return self.db.get_client_info(login)

    def get_other_client_info(self, login):
        return self.db.get_other_client_info(login)

    def read_users(self):
        readed_users = self.db.read_users()
        return readed_users

    def read_clients(self):
        readed_clients = self.db.read_clients()
        return readed_clients

    def read_zodiacs(self):
        readed_zodiacs = self.db.read_zodiacs()
        return readed_zodiacs

    def read_hairs(self):
        readed_hairs = self.db.read_hairs()
        return readed_hairs

    def read_eyes(self):
        readed_eyes = self.db.read_eyes()
        return readed_eyes
