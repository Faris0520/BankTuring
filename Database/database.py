import sqlite3

class Database:
    def __init__(self, nama_db="bank.db"):
        self.conn = sqlite3.connect(nama_db)
        self.cursor = self.conn.cursor()

    def inisialisasi(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS persons (
            national_identification_number TEXT PRIMARY KEY,
            name TEXT,
            birth TEXT,
            mother_name TEXT,
            family_card_number TEXT,
            postal_code TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            bank_account_number TEXT PRIMARY KEY,
            balance INTEGER,
            pin TEXT,
            national_identification_number TEXT,
            FOREIGN KEY (national_identification_number) REFERENCES persons(national_identification_number)
        )
        """)
# =================================================================
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created_at TEXT NOT NULL,
            transaction_type TEXT NOT NULL,
            from_name TEXT,
            from_account_number TEXT,
            to_name TEXT,
            to_account_number TEXT,
            amount INTEGER,
            balance_before INTEGER,
            balance_after INTEGER,
            notes TEXT
        )
        """)
        self.conn.commit()
        self._ensure_transaction_columns()
# ==================================================================        
    def tutup(self):
        self.conn.close()

    def _ensure_transaction_columns(self):
        self._ensure_column("transactions", "from_account_number", "TEXT")
        self._ensure_column("transactions", "to_account_number", "TEXT")

    def _ensure_column(self, table_name, column_name, column_type):
        self.cursor.execute(f"PRAGMA table_info({table_name})")
        columns = [row[1] for row in self.cursor.fetchall()]
        if column_name not in columns:
            self.cursor.execute(
                f"ALTER TABLE {table_name} ADD COLUMN {column_name} {column_type}"
            )
            self.conn.commit()
