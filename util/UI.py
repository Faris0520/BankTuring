import os

def clear() :
    os.system("cls")

def enter_to_continue():
    input("Tekan Enter Untuk Melanjutkan!")

def not_available_menu():
    print("Menu Tidak Tersedia!")
    enter_to_continue()

def header(word):
    print("="*21)
    print(f"===={word:^13}====")
    print("="*21)

def input_user(amount_choice):
    input_recomendation = "/".join(str(i) for i in range(1,amount_choice+1))
    return int(input(f"({input_recomendation})> "))
    

def menu_landing_page():
    print("Selamat Datang di Bank Turing, silahkan pilih Menu")
    print("1. Masuk")
    print("2. Buat Akun")
    print("3. Keluar")
    return input_user(3)

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



