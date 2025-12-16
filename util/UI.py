def header(word):
    print("="*21)
    print(f"===={word:^13}====")
    print("="*21)
    
def menu_landing_page():
    print("Selamat Datang di Bank Turing, silahkan pilih Menu")
    print("1. Masuk")
    print("2. Buat Akun")
    user_choice = int(input("(1/2)> "))
    if user_choice == 1 or user_choice == 2 :
        return user_choice
    else :
        return 0

def menu_login():
    print("Silahkan login ke akun Anda")
    account_number = input("Nomor Rekening: ")
    pin = input("PIN: ")
    return account_number, pin

def menu_main_banking():
    print("Pilih layanan yang ingin Anda gunakan:")
    print("1. Cek Saldo")
    print("2. Setor Tunai")
    print("3. Tarik Tunai")
    print("4. Transfer")
    print("5. Riwayat Transaksi")
    print("6. Keluar")
    user_choice = int(input("(1-6)> "))
    if 1 <= user_choice <= 6:
        return user_choice
    else:
        return 0

def show_error(message):
    print(f"ERROR: {message}")

def show_success(message):
    print(f"SUCCESS: {message}")

def confirm_action(action):
    confirmation = input(f"Apakah Anda yakin ingin {action}? (y/n): ")
    return confirmation.lower() == 'y'



