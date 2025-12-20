from Database.database import Database
from Repository.SqliteAccountRepository import SQLiteAccountRepository
from ProcessLogic.TransactionService import TransactionService
from util import ui



db = Database()
db.inisialisasi()

repo = SQLiteAccountRepository(db)
service = TransactionService(repo)

while True :
    ui.clear()
    ui.header("BANK TURING")
    user_choice = ui.menu_landing_page()
    match user_choice:
        case 2 :
            pass
        
        case 3 :
            break
        
        case _:
            ui.not_available_menu()
    
    




db.tutup()
