from .TransactionError import TransactionError
from datetime import datetime
from AccountPersonTemplate.Transaction import Transaction

class TransactionService:

    def __init__(self, account_repository, transaction_history_repository=None):
        self.account_repository = account_repository
        self.history_repo = transaction_history_repository

    def _log(self, transaction: Transaction):
        # optional dependency (tetap SOLID: service tidak tergantung sqlite langsung)
        if self.history_repo:
            self.history_repo.add(transaction)

    def deposit(self, account_number, amount):
        if amount <= 0:
            raise TransactionError("Jumlah deposit harus lebih dari 0")

        account = self.account_repository.get_by_account_number(account_number)
        if not account:
            raise TransactionError("Akun tidak ditemukan")

        balance_before = account.get_balance
        account.deposit(amount)
        self.account_repository.save(account)
        balance_after = account.get_balance

        self._log(Transaction(
            created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            transaction_type="DEPOSIT",
            from_name=account.get_person.get_name,
            from_account_number=account.get_bank_account_number,
            to_name=None,
            to_account_number=None,
            amount=amount,
            balance_before=balance_before,
            balance_after=balance_after,
            notes="Deposit berhasil"
        ))

        return account.get_balance

    def transfer(self, from_account_number, to_account_number, amount):
        if amount <= 0:
            raise TransactionError("Jumlah transfer harus lebih dari 0")

        from_account = self.account_repository.get_by_account_number(from_account_number)
        to_account = self.account_repository.get_by_account_number(to_account_number)

        if not from_account or not to_account:
            raise TransactionError("Akun pengirim atau penerima tidak ditemukan")

        if from_account.get_balance < amount:
            raise TransactionError("Saldo tidak mencukupi")

        balance_before = from_account.get_balance

        from_account.withdraw(amount)
        to_account.deposit(amount)

        self.account_repository.save(from_account)
        self.account_repository.save(to_account)

        balance_after = from_account.get_balance

        self._log(Transaction(
            created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            transaction_type="TRANSFER",
            from_name=from_account.get_person.get_name,
            from_account_number=from_account.get_bank_account_number,
            to_name=to_account.get_person.get_name,
            to_account_number=to_account.get_bank_account_number,
            amount=amount,
            balance_before=balance_before,
            balance_after=balance_after,
            notes="Transfer berhasil"
        ))

    def cek_saldo(self, account_number):
        account = self.account_repository.get_by_account_number(account_number)

        if not account:
            raise TransactionError("Akun tidak ditemukan")

        return account.get_balance
    
    def withdraw(self, account_number, amount):
        if amount <= 0:
            raise TransactionError("Jumlah tarik tunai harus lebih dari 0")

        account = self.account_repository.get_by_account_number(account_number)
        if not account:
            raise TransactionError("Akun tidak ditemukan")

        if account.get_balance < amount:
            raise TransactionError("Saldo tidak mencukupi")

        balance_before = account.get_balance
        account.withdraw(amount)
        self.account_repository.save(account)
        balance_after = account.get_balance

        self._log(Transaction(
            created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            transaction_type="WITHDRAW",
            from_name=account.get_person.get_name,
            from_account_number=account.get_bank_account_number,
            to_name=None,
            to_account_number=None,
            amount=amount,
            balance_before=balance_before,
            balance_after=balance_after,
            notes="Tarik tunai berhasil"
        ))

        return account.get_balance