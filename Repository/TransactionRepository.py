from abc import ABC, abstractmethod

class TransactionRepository(ABC):

    @abstractmethod
    def add(self, transaction):
        pass

    @abstractmethod
    def list_by_person_name(self, person_name, limit=20):
        pass