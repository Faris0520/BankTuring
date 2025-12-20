from abc import ABC, abstractmethod

class PersonRepository(ABC):

    def get_by_national_identification_number(self, national_identification_number):
        pass
    
    def save(self, person):
        pass