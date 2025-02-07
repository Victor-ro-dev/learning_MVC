import os
from typing import Dict

class PeopleRegisterView:
    def register_person_view(self) -> Dict:
        os.system('cls')

        print("Register a person\n\n")
        name = input('Enter the name of the person: ')
        age = input('Enter the age of the person: ')
        phone = input('Enter the phone number of the person: ')

        person_register_data = {
            'name': name,
            'age': age,
            'phone': phone
        }
        return person_register_data
    
    def registery_sucess_view(self, message: Dict) -> None:
        os.system('cls')
        success_message = f'''

        Registration successful
        -----------------------
        Tipo: {message["type"]}
        Registor: {message["count"]}
        Name: {message["attributes"]["name"]}
        Age: {message["attributes"]["age"]}

'''
        print(success_message)
        os.system('pause')

    def registery_error_view(self, error: str) -> None:
        os.system('cls')
        error_message = f'''

        Registration error
        -----------------------
        Erro: {error}
'''
        print(error_message)
        os.system('pause')