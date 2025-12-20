from AccountPersonTemplate.Person import Person
from AccountPersonTemplate.Account import Account
import random

class MakeAccountService:
    def __init__(self, person_repo, account_repo):
        self.person_repo = person_repo
        self.account_repo = account_repo
        
    
    def create_account(self, person_data, pin):
        person = Person(**person_data)
        self.person_repo.save(person)

        account = Account(person, pin)
        self.account_repo.save(account)

        return account