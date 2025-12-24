class LoginService:

    def __init__(self, account_repository, admin_service):
        self.repo = account_repository
        self.admin_service = admin_service

    def login(self, username: str, password: str):
        admin = self.admin_service.login(username, password)
        if admin:
            return admin

        account = self.repo.get_by_account_number(username)

        if not account:
            raise ValueError("Nomor rekening / Username tidak ditemukan")

        if account.get_pin != password:
            raise ValueError("PIN salah")

        return account