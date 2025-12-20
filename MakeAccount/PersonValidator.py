from datetime import datetime

class ValidationError(Exception):
    pass


class PersonValidator:

    @staticmethod
    def name_validation(name):
        if not name.strip():
            raise ValidationError("Nama tidak boleh kosong")

    @staticmethod
    def birth_validation(birth):
        try:
            datetime.strptime(birth, "%Y-%m-%d")
        except ValueError:
            raise ValidationError("Format tanggal lahir harus YYYY-MM-DD")

    @staticmethod
    def mother_name_validation(mother_name):
        if not mother_name.strip():
            raise ValidationError("Nama ibu tidak boleh kosong")

    @staticmethod
    def family_card_number_validation(kk):
        if not kk.isdigit() or len(kk) != 16:
            raise ValidationError("Nomor KK harus 16 digit angka")

    @staticmethod
    def national_identification_number_validation(nik):
        if not nik.isdigit() or len(nik) != 16:
            raise ValidationError("NIK harus 16 digit angka")

    @staticmethod
    def postal_code_validation(postal_code):
        if not postal_code.isdigit() or len(postal_code) != 5:
            raise ValidationError("Kode POS harus 5 digit angka")
