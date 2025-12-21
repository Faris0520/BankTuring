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
    account_number = input("Nomor Rekening: ")
    pin = input("PIN: ")
    return (account_number, pin)

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
    print("3. Tarik Tunai")
    print("4. Transfer")
    print("5. Riwayat Transaksi")
    print("6. Keluar")
    user_choice = input_user_choice(6)
    return ("Cek Saldo" if user_choice == 1
            else "Deposit" if user_choice == 2
            else "Tarik Tunai" if user_choice == 3
            else "Transfer" if user_choice == 4
            else "Riwayat Transaksi" if user_choice == 5
            else "Break" if user_choice == 6
            else "Other")

def show_transaction_history(transactions):
    print("=" * 36)
    print("RIWAYAT TRANSAKSI".center(36))
    print("=" * 36)

    if not transactions:
        print("Belum ada transaksi.")
        print("=" * 36)
        return

    for t in transactions:
        waktu = t.get_created_at
        jenis = t.get_transaction_type
        dari = t.get_from_name or "-"
        dari_rek = t.get_from_account_number or "-"
        ke = t.get_to_name or "-"
        ke_rek = t.get_to_account_number or "-"
        nominal = t.get_amount
        saldo_awal = t.get_balance_before
        saldo_akhir = t.get_balance_after
        catatan = t.get_notes or "-"

        print(f"{'Waktu':<14}: {waktu}")
        print(f"{'Jenis':<14}: {jenis}")
        print(f"{'Pengirim':<14}: {dari}")
        print(f"{'Rek. Pengirim':<14}: {dari_rek}")
        print(f"{'Penerima':<14}: {ke}")
        print(f"{'Rek. Penerima':<14}: {ke_rek}")
        if nominal is not None:
            print(f"{'Nominal':<14}: Rp {nominal:,}".replace(",", "."))
        if saldo_awal is not None:
            print(f"{'Saldo Awal':<14}: Rp {saldo_awal:,}".replace(",", "."))
        if saldo_akhir is not None:
            print(f"{'Saldo Akhir':<14}: Rp {saldo_akhir:,}".replace(",", "."))
        print(f"{'Catatan':<14}: {catatan}")
        print("-" * 36)

    print("=" * 36)
    
def print_receipt(
    transaction_type,
    from_name,
    from_account_number,
    to_name,
    to_account_number,
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
        print(f"{'Nama':<14}: {from_name}")
    if from_account_number:
        print(f"{'No. Rekening':<14}: {from_account_number}")
    if to_name:
        print(f"{'Nama Penerima':<14}: {to_name}")
    if to_account_number:
        print(f"{'No. Rekening Penerima':<14}: {to_account_number}")
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

def show_new_account_summary(account):
    person = account.get_person
    print("=" * 36)
    print("AKUN BERHASIL DIBUAT".center(36))
    print("=" * 36)
    print(f"{'Nama':<16}: {person.get_name}")
    print(f"{'NIK':<16}: {person.get_national_identification_number}")
    print(f"{'Nomor Rekening':<16}: {account.get_bank_account_number}")
    print(f"{'Saldo Awal':<16}: Rp {account.get_balance:,}".replace(",", "."))
    print("=" * 36)
    
def show_error(message):
    print(f"ERROR: {message}")

def show_success(message):
    print(f"SUCCESS: {message}")

def confirm_action(action):
    confirmation = input(f"Apakah Anda yakin ingin {action}? (y/n): ")
    return confirmation.lower() == 'y'
