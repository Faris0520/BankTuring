from abc import ABC, abstractmethod

class AccountRepository(ABC):

    @abstractmethod
    def get_by_person_name(self, bank_account_number):
        pass

    @abstractmethod
    def save(self, account):
        pass
