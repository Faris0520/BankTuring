from .TransactionError import TransactionError

class TransactionService:

    def __init__(self, account_repository):
        self.account_repository = account_repository

    def deposit(self, person_name, amount):
        if amount <= 0:
            raise TransactionError("Jumlah deposit harus lebih dari 0")

        account = self.account_repository.get_by_person_name(
            person_name
        )

        if not account:
            raise TransactionError("Akun tidak ditemukan")

        account.deposit(amount)
        self.account_repository.save(account)

        return account.get_balance

    def transfer(self, from_person_name, to_person_name, amount):
        if amount <= 0:
            raise TransactionError("Jumlah transfer harus lebih dari 0")

        from_account = self.account_repository.get_by_person_name(
            from_person_name
        )
        to_account = self.account_repository.get_by_person_name(
            to_person_name
        )

        if not from_account or not to_account:
            raise TransactionError("Akun pengirim atau penerima tidak ditemukan")

        if from_account.get_balance < amount:
            raise TransactionError("Saldo tidak mencukupi")

        from_account.withdraw(amount)
        to_account.deposit(amount)

        self.account_repository.save(from_account)
        self.account_repository.save(to_account)

    def cek_saldo(self, person_name):
        account = self.account_repository.get_by_person_name(person_name)

        if not account:
            raise TransactionError("Akun tidak ditemukan")

        return account.get_balance