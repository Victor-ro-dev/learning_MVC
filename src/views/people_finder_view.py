from typing import Dict
import os

class PeopleFinderView:
    def find_person_view(self) -> Dict:
        os.system('cls')

        print("Find a person\n\n")
        name = input('Deternime the name of the person: ')

        person_finder_data = {
            'name': name
        }
        return person_finder_data
    
    def find_sucess_view(self, message: Dict) -> None:
        os.system('cls')
        success_message = f'''
        Search successful
        -----------------------
        Tipe: {message["type"]}
        Registro: {message["count"]}
        Nome: {message["attributes"]["name"]}
        Idade: {message["attributes"]["age"]}
        Telefone: {message["attributes"]["phone"]}
'''
        print(success_message)
        os.system('pause')

    def find_error_view(self, error: str) -> None:
        os.system('cls')
        error_message = f'''
        Search error
        -----------------------
        Error: {error}

'''
        print(error_message)
        os.system('pause')