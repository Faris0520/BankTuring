class ValidationError(Exception):
    pass

class AccountValidator:

    @staticmethod
    def pin_validation(pin: str):
        if not pin.isdigit():
            raise ValidationError("PIN harus berupa angka")

        if len(pin) != 6:
            raise ValidationError("PIN harus 6 digit")

    @staticmethod
    def national_identification_number_validation(national_identification_number):
        if not national_identification_number.isdigit():
            raise ValidationError("NIK harus berupa angka")

        if len(national_identification_number) != 16:
            raise ValidationError("NIK harus 16 digit")

    @staticmethod
    def family_card_validation(family_card_number):
        if not family_card_number.isdigit():
            raise ValidationError("Nomor KK harus berupa angka")

        if len(family_card_number) != 16:
            raise ValidationError("Nomor KK harus 16 digit")
