from src.models.entities.person import Person

class __PersonRepository:
    def __init__(self):
       self.people = []

    def add_person(self, person: Person):
        self.people.append(person)                  

    def get_person(self, name: str):
        for person in self.people:
            if person.name == name:
                return person
        return None

person_repository = __PersonRepository()