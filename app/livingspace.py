from app.room import Room


class Livingspace(Room):
    def __init__(self, room_name, capacity, room_type):
        super().__init__(room_name, capacity, room_type)
        capacity = 4
        room_type = 'Livingspace'
        livingspaces_list = []
        self.livingspace_occupants_list = []

    def is_livingspace_assignable(self):
        if len(self.livingspace_occupants_list) < self.capacity:
            return True
        else:
            return False

    def assign_allocated_staff_livingspace(self, name):
        if len(self.livingspace_occupants_list) < self.capacity:
            self.livingspace_occupants_list.append(name)
            return True
        else:
            return False

    def len_livingspace_occupants_list(self):
        return len(self.livingspace_occupants_list)