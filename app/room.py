from abc import ABCMeta


class Room(object):
    __metaclass__ = ABCMeta

    capacity = 0
    room_type = ""

    def __init__(self, room_name, room_type):
        self.room_name = room_name
        self.room_type = room_type
        self.room_occupants_list = []

    def is_room_assignable(self, room_name):
        if len(room_name.self.room_occupants_list) < self.capacity:
            return True
        else:
            return False

    def len_room_occupants_list(self):
        return len(self.room_occupants_list)

    def add_person_to_room(self, person):
        if self.is_room_assignable(self.room_name):
            self.room_occupants_list.append(person)
            return True
        else:
            return False
