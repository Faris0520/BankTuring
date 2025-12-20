import os
from AccountPersonTemplate.Person import Person
from .PersonValidator import PersonValidator, ValidationError


class PersonInputForm:

    def set_person(self):
        while True:
            try:
                name = input(f"{'Nama':<30} : ")
                PersonValidator.name_validation(name)

                birth = input(f"{'Tanggal Lahir (YYYY-MM-DD)':<30} : ")
                PersonValidator.birth_validation(birth)

                mother_name = input(f"{'Nama Ibu':<30} : ")
                PersonValidator.mother_name_validation(mother_name)

                family_card_number = input(f"{'Nomor KK':<30} : ")
                PersonValidator.family_card_number_validation(family_card_number)

                national_identification_number = input(f"{'NIK':<30} : ")
                PersonValidator.national_identification_number_validation(national_identification_number)

                postal_code = input(f"{'Kode POS':<30} : ")
                PersonValidator.postal_code_validation(postal_code)

                return Person(
                    name,
                    birth,
                    mother_name,
                    family_card_number,
                    national_identification_number,
                    postal_code
                )

            except ValidationError as e:
                print("\nError:", e)
                input("Tekan Enter untuk mengulang...")
                os.system("cls" if os.name == "nt" else "clear")
