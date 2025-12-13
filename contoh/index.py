import sqlite3
import os

conn = sqlite3.connect("test.db")
cur = conn.cursor()

class Database:
    def tambah():
        os.system('cls')
        print("="*30)
        nama = str(input("Masukan nama: "))
        nim = str(input("Masukan NIM: "))
        prodi = str(input("Masukan prodi: "))
        print("="*30)

        try:
            cur.execute("""
            INSERT INTO mahasiswa (nama, nim, prodi)
            VALUES (?, ?, ?)
            """, (nama, nim, prodi))

            conn.commit()
            print("Berhasil memsaukkan data")
            input("\nTekan enter untuk keluar...")
        except Exception as e:
            print(f"Error {e}")

    def tampilkan():
        os.system('cls')
        print("="*30)
        cur.execute("SELECT * FROM mahasiswa")
        rows = cur.fetchall()
        
        for row in rows:
            print(row)
        print("="*30)
            
    def update():
        os.system('cls')
        print("="*30)
        prodi = str(input("Masukkan prodi: "))
        id = int(input("Masukkan id: "))
        print("="*30)
        cur.execute("""
                    UPDATE mahasiswa
                    SET prodi = ?
                    WHERE id = ?
                    """, (prodi, id))
        
        conn.commit()
        print("\nBerhasil mengupdate data")
        input("Tekan enter untuk keluar...")
        
    def delete():
        os.system('cls')
        Database.tampilkan()
        id = int(input("Masukkan id: "))
        cur.execute("DELETE FROM mahasiswa WHERE id= ?", (id,))
        conn.commit()
        print(f"\nBerhasil menghapus {id}!")
        input("Tekan enter untuk keluar...")

    def close():
        os.system('cls')
        conn.close()
        