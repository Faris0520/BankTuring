class Transaction:
    def __init__(
        self,
        created_at,
        transaction_type,
        from_name=None,
        from_account_number=None,
        to_name=None,
        to_account_number=None,
        amount=None,
        balance_before=None,
        balance_after=None,
        notes=None
    ):
        self.__created_at = created_at
        self.__transaction_type = transaction_type
        self.__from_name = from_name
        self.__from_account_number = from_account_number
        self.__to_name = to_name
        self.__to_account_number = to_account_number
        self.__amount = amount
        self.__balance_before = balance_before
        self.__balance_after = balance_after
        self.__notes = notes

    @property
    def get_created_at(self):
        return self.__created_at

    @property
    def get_transaction_type(self):
        return self.__transaction_type

    @property
    def get_from_name(self):
        return self.__from_name

    @property
    def get_from_account_number(self):
        return self.__from_account_number

    @property
    def get_to_name(self):
        return self.__to_name

    @property
    def get_to_account_number(self):
        return self.__to_account_number

    @property
    def get_amount(self):
        return self.__amount

    @property
    def get_balance_before(self):
        return self.__balance_before

    @property
    def get_balance_after(self):
        return self.__balance_after

    @property
    def get_notes(self):
        return self.__notes