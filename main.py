from Db.database import Database
from Repository.sqlite_account_repository import SQLiteAccountRepository
from ProcessLogic.TransactionService import TransactionService

db = Database()
db.inisialisasi()

repo = SQLiteAccountRepository(db)
service = TransactionService(repo)

service.setor("123456", 500000)
service.tarik("123456", 200000)

db.tutup()
