class Account :
    
    def __init__(self, balance, bank_account_number, pin,person):
        self.__balance = balance
        self.__bank_account_number = bank_account_number
        self.__pin = pin
        self.__person = person
        
    @property
    def get_balance(self):
        return self.__balance
    
    @property
    def get_pin(self):
        return self.__pin
    
    @property
    def get_bank_account_number(self):
        return self.__bank_account_number
    
    @property
    def get_person(self) :
        return self.__person
