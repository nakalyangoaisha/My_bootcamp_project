import random


from app.fellow import Fellow
from app.livingspace import Livingspace
from app.office import Office
from app.staff import Staff


class Dojo:
    def __init__(self):
        self.rooms_list = []
        self.people_list = []
        self.offices_list = []
        self.livingspaces_list = []
        self.fellows_list = []
        self.staff_list = []
        self.officeallocations_list = []

    def create_room(self, room_name, room_type):

        if isinstance(room_name, str) and isinstance(room_type, str):
            if room_name == '' or room_type == '':
                return 'room should have a name and a type'
            else:
                room = None
                if room_type is 'office':
                    room = Office('room_name')
                    self.offices_list.append(room)
                elif room_type is 'livingspace':
                    room = Livingspace('room_name', 'capacity', 'room_type')
                    self.livingspaces_list.append(room)
                if room is not None:
                    self.rooms_list.append(room)
                    return True
                else:
                    return False

    def add_person(self, name, position):
        if isinstance(name, str) and isinstance(position, str):
            if name == '' or position == '':
                return 'person should have a name and a position'
            else:
                person = None
                if position is 'fellow':
                    person = Fellow('name', 'position')
                    self.fellows_list.append(person)
                elif position is 'staff':
                    person = Staff('name', 'position')
                    self.staff_list.append(person)
                if person is not None:
                    self.people_list.append(person)
                    return True
                else:
                    return False

    def allocate_room(self, name, position):
        if isinstance(name, str) and isinstance(position, str):
            if name == '' or position == '':
                return 'person should have a name and position'
            else:
                if name in self.officeallocations_list and self.fellows_list:
                    return 'Fellow has already been allocated an office'
                else:
                    secure_random = random.SystemRandom()



















    def print_room(self, name):
        pass

    def print_allocations(self, ):
        pass


Dojo_instance = Dojo()
