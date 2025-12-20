from Database.database import Database
from Repository.SqliteAccountRepository import SQLiteAccountRepository
from ProcessLogic.TransactionService import TransactionService
from util import ui
from MakeAccount.PersonInputForm import PersonInputForm
from MakeAccount.AccountInputForm import AccountInputForm



db = Database()
db.inisialisasi()

repo = SQLiteAccountRepository(db)
service = TransactionService(repo)
person = PersonInputForm()
account = AccountInputForm()

while True :
    ui.clear()
    ui.header("BANK TURING")
    user_choice = ui.menu_landing_page()
    match user_choice:
        case 2 :
            person_info = person.set_person()
            account_info = account.set_account(person_info)
            repo.save_new_account(account_info)
            input()
        
        case 3 :
            break
        
        case _:
            ui.not_available_menu()


db.tutup()