import AccountValidator
import os

class AccountInputUI:
    def ambil_pin(self):
        while True:
            pin = input("Masukkan PIN (6 digit): ")
            try:
                AccountValidator.validasi_pin(pin)
                return pin
            except AccountValidator.ValidationError as e:
                print("Error:", e)
                input("Tekan Enter untuk Melanjutkan")
                os.system("cls")

    def ambil_data_person(self):
        while True:
            data = {
                "name": input(f"{'Nama':<30} : "),
                "birth": input("Tanggal Lahir : "),
                "mother_name": input("Nama Ibu : "),
                "family_card_number": input("Nomor KK : "),
                "national_identification_number": input("NIK : "),
                "postal_code": input("Kode POS : ")
            }
            try:
                AccountValidator.validasi_nomor_kk(data["family_card_number"])
                AccountValidator.validasi_nik(data["national_identification_number"])
                return data
            except AccountValidator.ValidationError as e:
                print("Error:", e)
                input("Tekan Enter untuk Melanjutkan")
                os.system("cls")
