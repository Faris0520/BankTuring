from Database.database import Database
from Repository.SqliteAccountRepository import SQLiteAccountRepository
from ProcessLogic.TransactionService import TransactionService
from util import UI

db = Database()
db.inisialisasi()

repo = SQLiteAccountRepository(db)
service = TransactionService(repo)



db.tutup()
