from typing import Dict
from src.models.repository.person_repository import person_repository
from src.models.entities.person import Person

class PeopleFinderController:
    def find_person(self, person_finder_informnations: Dict) -> Dict:
        try:
            self.validate_fields(person_finder_informnations)
            person = self.__find_person(person_finder_informnations)
            response = self.__format_response(person)
            return {'success': True, 'message': response}
        except Exception as e:
            return { 'success': False , 'error': str(e) }
        
    def validate_fields(self, person_finder_informnations) -> None:
        if not isinstance(person_finder_informnations['name'], str):
            raise Exception('Campo nome incorreto')
        
    def __find_person(self, person_finder_informnations: Dict) -> Person:
        name = person_finder_informnations['name']

        person = person_repository.get_person(name)
        if person is None:
            raise Exception('Pessoa não encontrada')
        return person
    
    def __format_response(self, person: Person) -> Dict:
        return { 
            "count": 1,
            "type": "Person",
            "attributes": {
                "name": person.name,
                "age": person.age,
                "phone": person.number
            }
        }