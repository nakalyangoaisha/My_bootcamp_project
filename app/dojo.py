import random

from app.fellow import Fellow
from app.livingspace import Livingspace
from app.office import Office
from app.staff import Staff


class Dojo:
    def __init__(self):
        self.rooms_dict = {}
        self.people_dict = {}
        self.offices = {'available': [], 'unavailable': []}
        self.livingspaces = {'available': [], 'unavailable': []}
        self.staff_office_allocations = {}
        self.staff_office_allocations_list = []
        self.fellow_office_allocations = {}
        self.fellow_office_allocations_list = []
        self.fellow_livingspace_allocations = {}
        self.fellow_livingspace_allocations_list = []
        self.unallocated_people_offices = {}
        self.unallocated_people_livingspaces = {}

    def create_room(self, room_name, room_type):

        if isinstance(room_name, str) and isinstance(room_type, str):
            if room_name == '' or room_type == '':
                return 'room should have a name and a type'
            else:
                if room_name in self.rooms_dict:
                    return 'Room already exists'
                if room_type is 'office':
                    office = Office(room_name, room_type)
                    self.rooms_dict[room_name] = office
                    self.offices['available'].append(office)
                    return True

                elif room_type is 'livingspace':
                    livingspace = Livingspace(room_name, room_type)
                    self.rooms_dict[room_name] = livingspace
                    self.livingspaces['available'].append(livingspace)
                    return True
        else:
            return 'room_name and room_type should be strings'

    def add_person(self, name, position, accommodate='No'):
        if isinstance(name, str) and isinstance(position, str) and isinstance(accommodate, str):
            if name == '' or position == '':
                return 'Name and position can not be empty strings'
            else:
                if name and position in self.people_dict:
                    return 'Person already exists'
                else:
                    if position == 'staff':
                        if accommodate == 'Yes':
                            return 'Staff cannot be accommodated'
                        elif accommodate == 'No':
                            staff = Staff(name, position, accommodate)
                            self.people_dict[name] = staff
                            self.allocate_room(name, 'office')
                            return True
                        elif not self.offices['available'] and accommodate == 'No':
                            return 'Please add more offices to the Dojo'
                    elif position == 'fellow':
                        if accommodate == 'No':
                            fellow = Fellow(name, position, accommodate)
                            self.people_dict[name] = fellow
                            self.allocate_room(fellow, 'office')
                        elif accommodate == 'Yes':
                            fellow = Fellow(name, position, accommodate)
                            if not self.livingspaces['available']:
                                return 'Please add more livingspaces to the Dojo'
                            elif not self.offices['available']:
                                return 'Please add more offices to the Dojo'
                            else:
                                self.people_dict[name] = fellow
                                self.allocate_room(name, 'office')
                                self.allocate_room(name, 'livingspace')
                                return True

        else:
            return 'Name and position should be strings'

    def allocate_room(self, name, room_type):
        if isinstance(name, str) and isinstance(room_type, str):
            if name == '' or room_type == '':
                return 'name and room_type can not be empty'
            else:
                if name not in self.people_dict.keys():
                    return 'Add person to people_dict first'
                else:
                    if room_type == 'office':
                        if self.people_dict[name].position == 'staff':
                            if name in self.staff_office_allocations.keys():
                                return 'Staff has already been allocated an office'
                            else:
                                self.staff_office_allocations[name] = random.choice(self.offices['available']).room_name
                                for room in self.offices['available']:
                                    if room.is_room_assignable():
                                        room.add_person_to_room(name)
                                        return True
                                    else:
                                        self.offices['unavailable'].append(room)
                                        self.unallocated_people_offices[name] = self.people_dict[name].position
                                        # while self.reallocate_unallocated() is not True:
                                        self.reallocate_unallocated()
                        elif self.people_dict[name].position == 'fellow':
                            if name in self.fellow_office_allocations.keys():
                                return 'Fellow has already been allocated an office'
                            else:
                                self.fellow_office_allocations[name] = random.choice(
                                    self.offices['available']).room_name

                                for room in self.offices['available']:
                                    if room.is_room_assignable():
                                        room.add_person_to_room(name)
                                        return True
                                    else:
                                        self.offices['unavailable'].append(room)
                                        self.unallocated_people_offices[name] = self.people_dict[name].position
                                        # while self.reallocate_unallocated() is not True:
                                        self.reallocate_unallocated()

                    elif self.people_dict[name].position == 'fellow' and room_type == 'livingspace':
                        if self.people_dict[name].accommodate == 'Yes':
                            self.fellow_livingspace_allocations[name] = random.choice(
                                self.livingspaces['available']).room_name
                        for room in self.livingspaces['available']:
                            if room.is_room_assignable():
                                room.add_person_to_room(name)
                                return True
                            # instead of false we can call the reallocate unallocated method in a loop
                            else:
                                self.offices['unavailable'].append(room)
                                self.unallocated_people_livingspaces[name] = self.people_dict[name].position
                                # while self.reallocate_unallocated() is not True:
                                self.reallocate_unallocated()
        else:
            return 'Name and room_type should be strings'

    def reallocate_unallocated(self):
        for name in self.unallocated_people_offices:
            if self.unallocated_people_offices[name] == 'staff':
                self.staff_office_allocations[name] = random.choice(self.offices['available']).room_name
                for room in self.offices['available']:
                    if room.is_room_assignable():
                        room.add_person_to_room(name)
                        del self.unallocated_people_offices[name]
                        return True
                    else:
                        self.offices['unavailable'].append(room)
            elif self.unallocated_people_offices[name] == 'fellow':
                self.fellow_office_allocations[name] = random.choice(
                    self.offices['available']).room_name
                for room in self.offices['available']:
                    if room.is_room_assignable():
                        room.add_person_to_room(name)
                        del self.unallocated_people_offices[name]
                        return True
                    else:
                        self.offices['unavailable'].append(room)

        for name in self.unallocated_people_livingspaces:
            if self.unallocated_people_livingspaces[name] == 'fellow':
                self.fellow_livingspace_allocations[name] = random.choice(
                    self.livingspaces['available']).room_name
                for room in self.livingspaces['available']:
                    if room.is_room_assignable():
                        room.add_person_to_room(name)
                        del self.unallocated_people_livingspaces[name]
                        return True

                    else:
                        self.offices['unavailable'].append(room)

    def print_room(self, room_name):
        if room_name in self.rooms_dict:
            for item in self.rooms_dict:
                if item == 'room_name':
                    return self.rooms_dict[room_name].room_occupants_list


Mydojo = Dojo()
print(Mydojo.create_room('aisha', 'office'))
print(Mydojo.create_room('noor', 'office'))
print(Mydojo.create_room('rukie', 'livingspace'))
print(Mydojo.add_person('aisha nakalyango', 'staff'))
print(Mydojo.add_person('aisha najuuma', 'fellow', 'Yes'))
print(Mydojo.add_person('hadia najuuma', 'fellow', 'Yes'))
print(Mydojo.add_person('noor najuuma', 'fellow', 'Yes'))
print(Mydojo.add_person('hadia najuuma', 'staff'))
print(Mydojo.add_person('hadia naksjbuma', 'fellow', 'Yes'))
print(Mydojo.add_person('hadia najk', 'fellow', 'Yes'))
print(Mydojo.people_dict)
print(len(Mydojo.people_dict))
# print(Mydojo.rooms_dict)
# print(Mydojo.allocate_room('aisha nakalyango', 'office'))
# print(Mydojo.allocate_room('aisha najuuma', 'office'))
# print(Mydojo.allocate_room('aisha najuuma', 'livingspace'))
# print(Mydojo.allocate_room('hadia najuuma', 'office'))
#print(Mydojo.rooms_dict['aisha'].len_room_occupants_list())
print(Mydojo.rooms_dict['noor'].len_room_occupants_list())
print(Mydojo.rooms_dict['aisha'].room_occupants_list)
print(Mydojo.print_room('aisha'))
print(Mydojo.staff_office_allocations)
print(Mydojo.fellow_office_allocations)
print(Mydojo.fellow_livingspace_allocations)
