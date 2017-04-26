from app.fellow import Fellow
from app.livingspace import Livingspace
from app.office import Office
from app.staff import Staff


class Dojo:
    def __init__(self):
        self.room_list = []
        self.people_list = []

    def create_room(self, room_name, room_type):

        if isinstance(room_name, str) and isinstance(room_type, str):
            if room_name == '' or room_type == '':
                return 'room should have a name and a type'
            else:
                room = None
                if room_type is 'Office':
                    room = Office('room_name')
                elif room_type is 'Living space':
                    room = Livingspace('room_name', 'capacity', 'room_type')
                if room is not None:
                    self.room_list.append(room)
                    return True
                else:
                    return False

    def add_person(self, person_name, position):
        if isinstance(person_name, str) and isinstance(position, str):
            if person_name == '' or position == '':
                return 'person should have a name and a position'
            else:
                person = None
                if position is 'fellow':
                    person = Fellow('name', 'position')
                elif position is 'staff':
                    person = Staff('name', 'position')
                if person is not None:
                    self.people_list.append(person)
                    return True
                else:
                    return False

    def print_room(self, name):
        pass

    def print_allocations(self, ):
        pass


Dojo_instance = Dojo()
