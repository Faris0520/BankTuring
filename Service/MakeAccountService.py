from AccountPersonTemplate.Person import Person
from AccountPersonTemplate.Account import Account




class MakeAccountService:

    @staticmethod
    def create_account(*account_info,**person_info):
        
        return Account(*account_info,person=Person(**person_info))