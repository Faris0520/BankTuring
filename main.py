from Database.database import Database
from Repository.SqliteAccountRepository import SQLiteAccountRepository
from Repository.SqliteTransactionRepository import SQLiteTransactionRepository
from Service.TransactionService import TransactionService
from Service.TransactionHistory import TransactionHistoryService
from util import UI
from MakeAccount.PersonInputForm import PersonInputForm
from MakeAccount.AccountInputForm import AccountInputForm
from Service.MakeAccountService import MakeAccountService
from Service.LoginService import LoginService
from Service.TransactionError import TransactionError

ui = UI
db = Database()
db.inisialisasi()

repo = SQLiteAccountRepository(db)
history_repo = SQLiteTransactionRepository(db)

login_service = LoginService(repo)
service = TransactionService(repo, history_repo)
history_service = TransactionHistoryService(history_repo)
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
            account_name = current_account.get_person.get_name
            account_number = current_account.get_bank_account_number
            user_choice_after_login = ui.menu_after_login(account_name)

            if user_choice_after_login == "Cek Saldo":
                ui.clear()
                ui.header("CEK SALDO")
                try:
                    saldo = service.cek_saldo(account_number)
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
                        account_number,
                        amount
                    )  
                except TransactionError as e:
                    print(e)
                except ValueError :
                    print("Input hanya dalam bentuk angka!")

                input("Tekan Enter...")
                
            elif user_choice_after_login == "Tarik Tunai":
                ui.clear()
                ui.header("TARIK TUNAI")

                try:
                    from_name = account_name
                    from_account_number = account_number

                    saldo_awal = service.cek_saldo(from_account_number)

                    amount = int(input("Jumlah Tarik Tunai: "))
                    saldo_setelah = service.withdraw(from_account_number, amount)

                    ui.clear()
                    ui.print_receipt(
                        transaction_type="WITHDRAW",
                        from_name=from_name,
                        from_account_number=from_account_number,
                        to_name=None,
                        to_account_number=None,
                        amount=amount,
                        balance_before=saldo_awal,
                        balance_after=saldo_setelah,
                        notes="Tarik tunai berhasil"
                    )

                except ValueError:
                    ui.show_error("Jumlah tarik tunai harus berupa angka")
                except TransactionError as e:
                    ui.show_error(str(e))

                ui.enter_to_continue()
                
            elif user_choice_after_login == "Transfer":
                ui.clear()
                ui.header("TRANSFER")

                try:
                    from_name = account_name
                    from_account_number = account_number
                    to_account_number = input("Nomor Rekening Tujuan: ").strip()

                    saldo_awal = service.cek_saldo(from_account_number)

                    amount = int(input("Jumlah Transfer: "))
                    service.transfer(from_account_number, to_account_number, amount)

                    saldo_akhir = service.cek_saldo(from_account_number)

                    target_account = repo.get_by_account_number(to_account_number)
                    target_name = target_account.get_person.get_name if target_account else to_account_number

                    ui.clear()
                    ui.print_receipt(
                        transaction_type="TRANSFER",
                        from_name=from_name,
                        from_account_number=from_account_number,
                        to_name=target_name,
                        to_account_number=to_account_number,
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

            elif user_choice_after_login == "Riwayat Transaksi":
                ui.clear()
                try:
                    items = history_service.get_history(
                        account_name,
                        limit=20
                    )
                    ui.show_transaction_history(items)
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
        new_account = MakeAccountService.create_account(*account_info, **person_info)
        repo.save_new_account(new_account)
        ui.clear()
        ui.show_new_account_summary(new_account)
        input("Tekan Enter untuk lanjut.")
    
    elif user_choice == "Break" :
        break
    
    else:
        ui.not_available_menu()


db.tutup()