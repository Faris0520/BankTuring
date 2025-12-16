from abc import ABC, abstractmethod

class AccountRepository(ABC):

    @abstractmethod
    def ambil_berdasarkan_no_rek(self, no_rek):
        pass

    @abstractmethod
    def simpan(self, account):
        pass
