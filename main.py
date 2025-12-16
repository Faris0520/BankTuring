from Db.database import Database
from Repository.sqlite_account_repository import SQLiteAccountRepository
from ProcessLogic.TransactionService import TransactionService
from util import UI

db = Database()
db.inisialisasi()

repo = SQLiteAccountRepository(db)
service = TransactionService(repo)



db.tutup()
