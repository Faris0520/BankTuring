class ValidationError(Exception):
    pass

class AccountValidator:

    @staticmethod
    def validasi_pin(pin: str):
        if not pin.isdigit():
            raise ValidationError("PIN harus berupa angka")

        if len(pin) != 6:
            raise ValidationError("PIN harus 6 digit")

    @staticmethod
    def validasi_nik(nik: str):
        if not nik.isdigit():
            raise ValidationError("NIK harus berupa angka")

        if len(nik) != 16:
            raise ValidationError("NIK harus 16 digit")

    @staticmethod
    def validasi_nomor_kk(kk: str):
        if not kk.isdigit():
            raise ValidationError("Nomor KK harus berupa angka")

        if len(kk) != 16:
            raise ValidationError("Nomor KK harus 16 digit")
