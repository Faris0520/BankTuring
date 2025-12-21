from .TransactionError import TransactionError

class TransactionHistoryService:
    def __init__(self, transaction_history_repository):
        self.history_repo = transaction_history_repository

    def get_history(self, person_name, limit=20):
        if not person_name or not str(person_name).strip():
            raise TransactionError("Nama rekening tidak valid")

        return self.history_repo.list_by_person_name(person_name, limit)