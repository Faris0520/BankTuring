from index import Database as db
import os
    
while True:
    os.system('cls')
    print("="*30)
    print("Pilih:\n1. Tambah\n2. Tampilkan\n3. Update\n4. Delete\n5. Keluar")
    print("="*30)
    pilihan = input("\nMasukkan pilihan: ")

    if pilihan == "1":
        db.tambah()
    elif pilihan == "2":
        db.tampilkan()
        input("\nTekan enter untuk keluar...")
    elif pilihan == "3":
        db.update()
    elif pilihan == "4":
        db.delete()
    elif pilihan == "5":
        db.close()
        print("Keluar dari program.")
        print("="*30)
        break
    else:
        print("Pilihan tidak valid, coba lagi.")
        print("="*30)