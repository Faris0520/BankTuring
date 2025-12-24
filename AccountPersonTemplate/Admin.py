class Admin:

    def __init__(self, username: str, password: str):
        self.__username = username
        self.__password = password

    @property
    def get_username(self):
        return self.__username

    @property
    def get_password(self):
        return self.__password
