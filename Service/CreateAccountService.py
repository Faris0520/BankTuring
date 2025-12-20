from AccountPersonTemplate.Person import Person
from AccountPersonTemplate.Account import Account

class AccountRegistrationService:
    def __init__(self, account_repository):
        self.account_repository = account_repository

    def register_account(self, person_data: dict, account_data: dict):
        # Di sini kamu bisa mapping dict → entity sebenarnya
        # Contoh sederhana (sesuaikan dengan constructor Person & Account kamu):

        person = Person(
            name=person_data["name"],
            birth=person_data["birth"],
            mother_name=person_data["mother_name"],
            family_card_number=person_data["family_card_number"],
            national_identification_number=person_data["national_identification_number"],
            postal_code=person_data["postal_code"],
        )

        account = Account(
            bank_account_number=account_data["bank_account_number"],
            pin=account_data["pin"],
            balance=account_data["balance"],
            owner=person,
        )

        self.account_repository.save_new_account(account)
        return account