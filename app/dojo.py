from random import randint

from livingspace import Livingspace
from office import Office
from staff import Staff


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
        self.unallocated_people = []

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
                            self.accommodate = 'No'
                            return 'Staff cannot be accommodated'
                        elif accommodate == 'No':
                            staff = Staff(name, position)
                            self.people_dict[name] = staff
                            self.allocate_room(staff, 'office')
                            return True
                        elif not self.offices['available'] and accommodate == 'No':
                            return 'Please add more offices to the Dojo'

                    elif position == 'fellow':
                        fellow = Fellow(name, position)
                        if accommodate == 'Yes':
                            if not self.livingspaces['available']:
                                return 'Please add more livingspaces to the Dojo'
                            elif not self.offices['available']:
                                return 'Please add more offices to the Dojo'
                            else:
                                self.people_dict[name] = fellow
                                self.allocate_room(fellow, 'livingspace')
                                return True
                        else:
                            self.people_dict[name] = fellow
                            self.allocate_room(fellow, 'office')
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
                                self.staff_office_allocations[name] = self.offices['available'][
                                    randint(0, (len(self.offices['available']) - 1))]
                                self.staff_office_allocations_list.append(self.staff_office_allocations)
                                for room in self.offices['available']:
                                    if not room.is_room_assignable():
                                        self.offices['unavailable'].append(room)
                                        self.offices['available'].remove(room)
                                        print('%s has reached its maximum capacity') % room
                                        self.unallocated_people.append(name)
                                    elif room.is_room_assignable:
                                        room.add_person_to_room(name)
                                        return True
                        elif self.people_dict[name].position == 'fellow':
                            if name in self.fellow_office_allocations.keys():
                                return 'Fellow has already been allocated an office'
                            else:
                                self.fellow_office_allocations[name] = self.offices['available'][
                                    randint(0, (len(self.offices['available']) - 1))]
                                self.fellow_office_allocations_list.append(self.fellow_office_allocations)
                                for room in self.offices['available']:
                                    if not room.is_room_assignable:
                                        self.offices['unavailable'].append(room)
                                        self.offices['available'].remove(room)
                                        print('%s has reached its maximum capacity') % room
                                        self.unallocated_people.append(name)
                                    elif room.is_room_assignable:
                                        room.add_person_to_room(name)
                                        return True

                    else:
                        if room_type == 'livingspace':
                            if self.people_dict[name].accommodate == 'Yes':
                                self.fellow_office_allocations['office'] = self.offices['available'][
                                    randint(0, (len(self.offices['available']) - 1))]
                                self.fellow_livingspace_allocations_list.append(self.staff_office_allocations)
                                for room in self.livingspaces['available']:
                                    if not room.is_room_assignable:
                                        self.offices['unavailable'].append(room)
                                        self.offices['available'].remove(room)
                                        print('%s has reached its maximum capacity') % room
                                        self.unallocated_people.append(name)
                                    elif room.is_room_assignable:
                                        room.add_person_to_room(name)

        else:
            return 'Name and room_type should be strings'
            # def reallocate_person(self, name, room_name):
            #     available_rooms = []
            #     for room in self.offices['available']:
            #         available_rooms.append(room)
            #     for room in self.livingspaces['available']:
            #         available_rooms.append(room)
            #     for name in self.people_dict.keys():
            #         if name in self.unallocated_people:
            #             pass

    def print_room(self, room_name):
        if room_name in self.rooms_dict:
           for item in self.rooms_dict:
               if item == 'room_name':
                print(room_name.room_occupants_list)


Mydojo = Dojo()
print(Mydojo.create_room('aisha', 'office'))
print(Mydojo.create_room('noor', 'office'))
print(Mydojo.create_room('rukie', 'livingspace'))
print(Mydojo.add_person('aisha nakalyango', 'staff'))
print(Mydojo.add_person('aisha najuuma', 'fellow'))
print(Mydojo.add_person('hadia najuuma', 'fellow', 'Yes'))
print(Mydojo.people_dict)
print(Mydojo.rooms_dict)
print(Mydojo.allocate_room('aisha nakalyango', 'office'))
print(Mydojo.allocate_room('aisha najuuma', 'office'))
print(Mydojo.allocate_room('hadia najuuma', 'office'))
print(Mydojo.allocate_room('hadia najuuma', 'livingspace'))
print(Mydojo.rooms_dict['aisha'].len_room_occupants_list())
print(Mydojo.rooms_dict['noor'].len_room_occupants_list())
print(Mydojo.rooms_dict['aisha'].room_occupants_list)
Mydojo.print_room('aisha')
print(Mydojo.staff_office_allocations)
print(Mydojo.fellow_office_allocations)
