from Database.database import Database
from Repository.SqliteAccountRepository import SQLiteAccountRepository
from Service.TransactionService import TransactionService
from util import ui
from MakeAccount.PersonInputForm import PersonInputForm
from MakeAccount.AccountInputForm import AccountInputForm
from Service.MakeAccountService import MakeAccountService
from Service.LoginService import LoginService
from Service.TransactionError import TransactionError


db = Database()
db.inisialisasi()

repo = SQLiteAccountRepository(db)
login_service = LoginService(repo)
service = TransactionService(repo)
person = PersonInputForm()
account = AccountInputForm()


    
while True :
    ui.clear()
    ui.header("BANK TURING")
    user_choice = ui.menu_landing_page()
    
    if user_choice == "Masuk" :
        current_account = None
        
        try :
            ui.clear()
            ui.header("LOGIN")
            login_information = ui.menu_login()
            current_account = login_service.login(*login_information)
        
        
        except ValueError as e:
            print(e)
            ui.enter_to_continue()
            continue
        
        if not current_account:
            continue
        
        while True:
            ui.clear()
            ui.header("BANK TURING")
            user_choice_after_login = ui.menu_after_login(current_account.get_person.get_name)

            if user_choice_after_login == "Cek Saldo":
                ui.clear()
                ui.header("CEK SALDO")
                try:
                    saldo = service.cek_saldo(current_account.get_person.get_name)
                    print(f"Saldo Anda: Rp {saldo:,},-")
                except TransactionError as e:
                    print(e)

                input("Tekan Enter...")
                
            elif user_choice_after_login == "Deposit":
                ui.clear()
                ui.header("DEPOSIT")

                try:
                    amount = int(input("Jumlah Deposit: "))
                    saldo_baru = service.deposit(
                        current_account.get_person.get_name,
                        amount
                    )  
                except TransactionError as e:
                    print(e)
                except ValueError :
                    print("Input hanya dalam bentuk angka!")

                input("Tekan Enter...")
                
            elif user_choice_after_login == "Transfer":
                ui.clear()
                ui.header("TRANSFER")

                try:
                    from_name = current_account.get_person.get_name
                    to_name = input("Nama Rekening Tujuan: ").strip()

                    saldo_awal = service.cek_saldo(from_name)

                    amount = int(input("Jumlah Transfer: "))
                    service.transfer(from_name, to_name, amount)

                    saldo_akhir = service.cek_saldo(from_name)

                    ui.clear()
                    ui.print_receipt(
                        transaction_type="TRANSFER",
                        from_name=from_name,
                        to_name=to_name,
                        amount=amount,
                        balance_before=saldo_awal,
                        balance_after=saldo_akhir,
                        notes="Transfer berhasil"
                    )

                except ValueError:
                    ui.show_error("Jumlah transfer harus berupa angka")
                except TransactionError as e:
                    ui.show_error(str(e))

                ui.enter_to_continue()


            elif user_choice_after_login == "Break":
                break

            else:
                ui.not_available_menu()
                input("Tekan Enter...")

    elif user_choice == "Buat Akun" :
        person_info = person.set_person()   
        account_info = account.set_account()
        repo.save_new_account(MakeAccountService.create_account(*account_info,**person_info)) 
        input("Akun berhasil dibuat! Tekan Enter untuk lanjut.")
    
    elif user_choice == "Break" :
        break
    
    else:
        ui.not_available_menu()


db.tutup()