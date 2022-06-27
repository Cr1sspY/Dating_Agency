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