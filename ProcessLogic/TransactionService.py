class TransactionService:
    
    def __init__(self, account_repository):
        self.account_repository = account_repository

    def setor(self, no_rek, jumlah):
        akun = self.account_repository.get_by_bank_account_number(no_rek)
        akun.setor(jumlah)
        self.account_repository.save(akun)

    def tarik(self, no_rek, jumlah):
        akun = self.account_repository.get_by_bank_account_number(no_rek)
        akun.tarik(jumlah)
        self.account_repository.save(akun)
