from .PersonRepository import PersonRepository
from AccountPersonTemplate.Person import Person

class PersonRepositoryDB(PersonRepository):

    def __init__(self, database):
        self.db = database

    def save(self, person):
        query = """
            INSERT INTO persons (national_identification_number, name, birth, mother_name, family_card_number, postal_code)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        self.db.cursor.execute(query, (
            person.get_national_identification_number(),
            person.get_name(),
            person.get_birth(),
            person.get_mother_name(),
            person.get_family_card_number(),
            person.get_postal_code()
        ))
        self.db.conn.commit()

    def get_by_national_identification_number(self, national_identification_number):
        query = "SELECT  name, birth, mother_name, family_card_number,national_identification_number, postal_code FROM persons WHERE national_identification_number=?"
        result = self.db.cursor.execute(query, (national_identification_number,)).fetchone()

        if result is None:
            return None

        return Person(
            name=result[0],
            birth=result[1],
            mother_name=result[2],
            family_card_number=result[3],
            national_identification_number = result[4],
            postal_code=result[5]
        )