from abc import ABC, abstractmethod

class PersonRepository(ABC):

    def get_by_nik(self, nik):
        pass
    
    def save(self, person):
        pass