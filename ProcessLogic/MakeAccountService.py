from AccountPerson.person import Person
from AccountPerson.Account import Account
import random

class MakeAccountService:
    
    def __init__(self):
        print("silahkan isi Data di bawah ini :")
        self.name = input(f"{'Nama ':<30} :")
        self.birth = input(f"{'Tanggal Lahir(yyyy/mm/dd) ':<30} :")
        self.mother_name = input(f"{'Nama ibu ':<30} :")
        self.family_card_number = input(f"{'Nomor KK ':<30} :")
        self.national_identification_number = input(f"{'NIK ':<30} :")
        self.postal_code = input(f"{'Kode POS ':<30} :")
        
    
    def confirm_data(self):
        print("Berikut Adalah Data yang Anda isikan :")
        print(f"{'Nama ':<30} : {self.name}")
        print(f"{'Tanggal Lahir ':<30} : {self.birth}")
        print(f"{'Nama Ibu ':<30} : {self.mother_name}")
        print(f"{'Nomor KK ':<30} : {self.family_card_number}")
        print(f"{'NIK ':<30} : {self.national_identification_number}")
        print(f"{'Kode POS ':<30} : {self.postal_code}")
        print("\nData sudah benar dan lanjutkan ke pembuatan akun?")
        confirmation_user_data = input("(y/n)>")
        return confirmation_user_data
    
    def set_pin(self):
        pin = input(f"{'Masukkan PIN (6 digit)':<30} :")
        return pin
        
    def generate_account_balance(self):
        pass
    
    def create_account(self,bank_account_number,pin,person):
        person = Person(
            name=self.name,
            birth=self.birth,
            mother_name=self.mother_name,
            family_card_number=self.family_card_number,
            national_identification_number=self.national_identification_number,
            postal_code=self.postal_code
        )
        default_balance = 0
        
        account = Account(default_balance,person)
        print(f"Akun berhasil dibuat dengan nomor rekening: {account.account_number}")
        return account
