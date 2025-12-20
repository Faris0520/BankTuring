class Person :
    
    
    def __init__(self, name, birth, mother_name, family_card_number, national_identification_number, postal_code):
        self.__name = name
        self.__birth = birth
        self.__mother_name = mother_name
        self.__family_card_number = family_card_number
        self.__national_identification_number = national_identification_number
        self.__postal_code = postal_code
    
    @property
    def get_name(self) :
        return self.__name
    
    @property
    def get_birth(self) :
        return self.__birth
    
    @property
    def get_mother_name(self) :
        return self.__mother_name
    
    @property
    def get_national_identification_number(self) :
        return self.__national_identification_number
    
    @property
    def get_postal_code(self) :
        return self.__postal_code
    
    @property
    def get_family_card_number(self) :
        return self.__family_card_number