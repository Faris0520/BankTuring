class LoginService:

    def __init__(self, account_repository):
        self.repo = account_repository

    def login(self, account_number: str, pin: str):
        account = self.repo.get_by_person_name(account_number)

        if not account:
            raise ValueError("Nomor rekening tidak ditemukan")

        if account.get_pin != pin:
            raise ValueError("PIN salah")

        return account