class Phonebook:
    def __init__(self):
        self.__i_d = 0
        self.__username = ''
        self.__password = ''

    def set_id(self, i_d: int):
        self.__i_d = i_d

    def get_id(self):
        return self.__i_d

    def set_username(self, username: str):
        self.__username = username

    def get_username(self):
        return self.__username

    def set_password(self, password: str):
        self.__password = password

    def get_password(self):
        return self.__password
