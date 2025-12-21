from .TransactionRepository import TransactionRepository
from AccountPersonTemplate.Transaction import Transaction

class SQLiteTransactionRepository(TransactionRepository):
    def __init__(self, database):
        self.db = database

    def add(self, transaction):
        cur = self.db.cursor
        cur.execute("""
        INSERT INTO transactions
            (created_at, transaction_type,
             from_name, from_account_number,
             to_name, to_account_number,
             amount, balance_before, balance_after, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            transaction.get_created_at,
            transaction.get_transaction_type,
            transaction.get_from_name,
            transaction.get_from_account_number,
            transaction.get_to_name,
            transaction.get_to_account_number,
            transaction.get_amount,
            transaction.get_balance_before,
            transaction.get_balance_after,
            transaction.get_notes
        ))
        self.db.conn.commit()

    def list_by_person_name(self, person_name, limit=20):
        cur = self.db.cursor
        cur.execute("""
     SELECT created_at, transaction_type,
         from_name, from_account_number,
         to_name, to_account_number,
         amount, balance_before, balance_after, notes
        FROM transactions
        WHERE from_name = ? OR to_name = ?
        ORDER BY id DESC
        LIMIT ?
        """, (person_name, person_name, limit))

        rows = cur.fetchall()
        return [
            Transaction(
                created_at=row[0],
                transaction_type=row[1],
                from_name=row[2],
                from_account_number=row[3],
                to_name=row[4],
                to_account_number=row[5],
                amount=row[6],
                balance_before=row[7],
                balance_after=row[8],
                notes=row[9]
            )
            for row in rows
        ]