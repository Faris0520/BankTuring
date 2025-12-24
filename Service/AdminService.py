from AccountPersonTemplate.Admin import Admin


class AdminService:

    def __init__(self):
        # ADMIN DITENTUKAN SISTEM
        self.__admin = Admin(
            username="admin",
            password="admin123"
        )

    def login(self, username: str, password: str):
        if self.__admin.get_username != username:
            return None

        if self.__admin.get_password != password:
            return None

        return self.__admin
