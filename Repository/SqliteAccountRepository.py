from AccountPersonTemplate.Account import Account
from AccountPersonTemplate.Person import Person
from .AccountRepository import AccountRepository

class SQLiteAccountRepository(AccountRepository):
    def __init__(self, database):
        self.db = database

    def get_by_bank_account_number(self, bank_account_number):
        cur = self.db.cursor
        cur.execute("""
        SELECT a.balance, a.bank_account_number, a.pin,
               p.name, p.birth, p.mother_name,
               p.family_card_number, p.nik, p.postal_code
        FROM accounts a
        JOIN persons p ON a.person_nik = p.nik
        WHERE a.bank_account_number = ?
        """, (bank_account_number,))

        row = cur.fetchone()
        if not row:
            return None

        balance, bank_account_number, pin, *person_data = row
        person = Person(*person_data)

        return Account(balance, bank_account_number, pin, person)

    def save(self, account):
        cur = self.db.cursor
        cur.execute("""
        UPDATE accounts SET balance = ?
        WHERE bank_account_number = ?
        """, (account.balance, account.bank_account_number))
        self.db.conn.commit()
