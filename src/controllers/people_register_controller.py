from typing import Dict
from src.models.repository.person_repository import person_repository
from src.models.entities.person import Person

class PeopleRegisterController:
    def register(self, new_person_informations: Dict)-> Dict:
        try:
            self.__validate_fields(new_person_informations)
            self.__register_person(new_person_informations)
            response = self.__format_response(new_person_informations)
            return {'success': True, 'message': response}
        except Exception as e:
            return { 'success': False , 'error': str(e) }
    
    def __validate_fields(self, new_person_informations) -> None:
        if not isinstance(new_person_informations['name'], str):
            raise Exception('Campo nome incorreto')
        
        try: int(new_person_informations['age'])
        except: raise Exception('Campo idade incorreto')

        try: int(new_person_informations['phone'])
        except: raise Exception('Campo telefone incorreto')

    def __register_person(self, new_person_informations: Dict) -> None:
        new_person = Person(
            name=new_person_informations['name'],
            age=new_person_informations['age'],
            number=new_person_informations['phone']
        )
        person_repository.add_person(new_person)

    def __format_response(self, new_person_informations: Dict) -> Dict:
        return { 
            "count": 1,
            "type": "Person",
            "attributes": new_person_informations
        }
       