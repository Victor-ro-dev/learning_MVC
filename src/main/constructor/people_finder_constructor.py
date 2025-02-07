from src.views.people_finder_view import PeopleFinderView
from src.controllers.people_finder_controller import PeopleFinderController

def people_finder_constructor():
    people_finder_view = PeopleFinderView()
    people_finder_controller = PeopleFinderController()
    #controller

    people_finder_information = people_finder_view.find_person_view()
    response = people_finder_controller.find_person(people_finder_information)
    #enviar para o controller

    if response['success']:
        people_finder_view.find_sucess_view(response['message'])

    else:   
        people_finder_view.find_error_view(response['error'])