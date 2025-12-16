def header(word):
    print("="*21)
    print(f"===={word:^13}====")
    print("="*21)
    
def menu_landing_page():
    print("Selamat Datang di Bank Turing,Silahkan Pilih menu")
    print("1. Masuk")
    print("2. Buat Akun")
    user_choice = int(input("(1/2)> "))
    if user_choice == 1 or user_choice == 2 :
        return user_choice
    else :
        return 0



