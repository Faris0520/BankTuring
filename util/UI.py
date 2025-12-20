import os
from datetime import datetime

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

def input_user_choice(amount_choice):
    input_recomendation = "/".join(str(i) for i in range(1,amount_choice+1))
    return int(input(f"({input_recomendation})> "))
    

def menu_login():
    print("Silahkan login ke akun Anda")
    name = input("Nama Rekening: ")
    pin = input("PIN: ")
    return (name, pin)

def menu_landing_page():
    print("Selamat Datang di Bank Turing, silahkan pilih Menu")
    print("1. Masuk")
    print("2. Buat Akun")
    print("3. Keluar")
    user_choice = input_user_choice(3)
    return ("Masuk" if user_choice == 1
            else "Buat Akun" if user_choice == 2
            else "Break" if user_choice == 3
            else "Other")

def menu_after_login(user_name):
    print(f"Selamat Datang {user_name}! Silahkan pilih Menu")
    print("1. Cek Saldo")
    print("2. Deposit")
    print("3. Transfer")
    print("4. Keluar")
    user_choice = input_user_choice(4)
    return ("Cek Saldo" if user_choice == 1
            else "Deposit" if user_choice == 2
            else "Transfer" if user_choice == 3
            else "Break" if user_choice == 4
            else "Other")

def print_receipt(
    transaction_type,
    from_name,
    to_name,
    amount,
    balance_before,
    balance_after,
    notes
):
    """
    Cetak struk transaksi sederhana untuk CLI.
    Semua parameter opsional agar bisa dipakai untuk Cek Saldo, Deposit, Transfer, dll.
    """
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("=" * 36)
    print("BANK TURING".center(36))
    print("STRUK TRANSAKSI".center(36))
    print("=" * 36)
    print(f"{'Waktu':<14}: {now}")
    print(f"{'Jenis':<14}: {transaction_type}")

    if from_name:
        print(f"{'Dari':<14}: {from_name}")
    if to_name:
        print(f"{'Ke':<14}: {to_name}")
    if amount is not None:
        print(f"{'Nominal':<14}: Rp {amount:,}".replace(",", "."))

    if balance_before is not None:
        print(f"{'Saldo Awal':<14}: Rp {balance_before:,}".replace(",", "."))
    if balance_after is not None:
        print(f"{'Saldo Akhir':<14}: Rp {balance_after:,}".replace(",", "."))

    if notes:
        print(f"{'Catatan':<14}: {notes}")

    print("-" * 36)
    print("Terima kasih telah bertransaksi".center(36))
    print("=" * 36)
    
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
