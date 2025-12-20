import os
import random
from AccountPersonTemplate.Account import Account
from .AccountValidator import AccountValidator, ValidationError


class AccountInputForm:


    default_balance = 0
    
    def generate_account_number(self):
        return "".join(str(random.randint(0, 9)) for _ in range(10))

    def set_account(self,person):
        while True:
            try:
                # generate nomor rekening
                account_number = self.generate_account_number()

                # input PIN
                pin = input(f"{'PIN (6 digit)': <30} : ")
                AccountValidator.pin_validation(pin)

                return Account(
                    AccountInputForm.default_balance,
                    account_number,
                    pin,
                    person
                )

            except ValidationError as e:
                print("\nError:", e)
                input("Tekan Enter untuk mengulang...")
                os.system("cls" if os.name == "nt" else "clear")