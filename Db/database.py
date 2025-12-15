import sqlite3

class Database:
    def __init__(self, nama_db="bank.db"):
        self.conn = sqlite3.connect(nama_db)
        self.cursor = self.conn.cursor()

    def inisialisasi(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS persons (
            nik TEXT PRIMARY KEY,
            name TEXT,
            birth TEXT,
            mother_name TEXT,
            family_card_number TEXT,
            postal_code TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            no_rek TEXT PRIMARY KEY,
            balance INTEGER,
            pin TEXT,
            person_nik TEXT,
            FOREIGN KEY (person_nik) REFERENCES persons(nik)
        )
        """)
        self.conn.commit()

    def tutup(self):
        self.conn.close()
