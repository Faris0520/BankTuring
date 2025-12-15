from AccountPerson.Account import Account
from AccountPerson.person import Person
from .Account_repository import AccountRepository

class SQLiteAccountRepository(AccountRepository):
    def __init__(self, database):
        self.db = database

    def ambil_berdasarkan_no_rek(self, no_rek):
        cur = self.db.cursor
        cur.execute("""
        SELECT a.balance, a.no_rek, a.pin,
               p.name, p.birth, p.mother_name,
               p.family_card_number, p.nik, p.postal_code
        FROM accounts a
        JOIN persons p ON a.person_nik = p.nik
        WHERE a.no_rek = ?
        """, (no_rek,))

        row = cur.fetchone()
        if not row:
            return None

        balance, no_rek, pin, *person_data = row
        person = Person(*person_data)

        return Account(balance, no_rek, pin, person)

    def simpan(self, account):
        cur = self.db.cursor
        cur.execute("""
        UPDATE accounts SET balance = ?
        WHERE no_rek = ?
        """, (account.balance, account.no_rek))
        self.db.conn.commit()
