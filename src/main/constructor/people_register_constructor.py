from src.views.people_register_view import PeopleRegisterView
from src.controllers.people_register_controller import PeopleRegisterController

def people_register_constructor():
    people_register_view = PeopleRegisterView()
    #controller
    people_register_controller = PeopleRegisterController()

    people_register_information = people_register_view.register_person_view()
    response = people_register_controller.register(people_register_information)

    if response['success']:
        people_register_view.registery_sucess_view(response['message'])
    else:
        people_register_view.registery_error_view(response['error'])
    
