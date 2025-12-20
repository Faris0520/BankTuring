from AccountPersonTemplate.Account import Account
from AccountPersonTemplate.Person import Person
from .AccountRepository import AccountRepository

class SQLiteAccountRepository(AccountRepository):
    def __init__(self, database):
        self.db = database

    def get_by_person_name(self, name):
        cur = self.db.cursor
        cur.execute("""
        SELECT a.balance, a.bank_account_number, a.pin,
            p.name, p.birth, p.mother_name,
            p.family_card_number, p.national_identification_number, p.postal_code
        FROM accounts a
        JOIN persons p ON a.national_identification_number = p.national_identification_number
        WHERE p.name = ?
        """, (name,))

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
        """, (account.get_balance, account.get_bank_account_number))
        self.db.conn.commit()

    def save_new_account(self, account):
        """
        Insert akun baru + data person ke database.
        """
        cur = self.db.cursor

        person = account.get_person
        
        cur.execute("""
        INSERT OR IGNORE INTO persons
            (national_identification_number, name, birth, mother_name, family_card_number, postal_code)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (
            person.get_national_identification_number,
            person.get_name,
            person.get_birth,
            person.get_mother_name,
            person.get_family_card_number,
            person.get_postal_code,
        ))

        # insert ke tabel accounts
        cur.execute("""
        INSERT INTO accounts
            (balance, bank_account_number, pin, national_identification_number)
        VALUES (?, ?, ?, ?)
        """, (
            account.get_balance,
            account.get_bank_account_number,
            account.get_pin,
            person.get_national_identification_number,
        ))

        self.db.conn.commit()