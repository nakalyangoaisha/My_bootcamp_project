from app.room import Room


class Office(Room):
    def __init__(self, room_name):
        capacity = 6
        room_type = 'office'
        Room.__init__(self, room_name, capacity, room_type)
        self.office_occupants_list = []

    def is_office_assignable(self):
        if len(self.office_occupants_list) < self.capacity:
            return True
        else:
            return False

    def assign_allocated_staffandfellows_office(self, name):
        if len(self.office_occupants_list) < self.capacity:
            self.office_occupants_list.append(name)
            return True
        else:
            return False

    def len_office_occupants_list(self):
        return len(self.office_occupants_list)


        # Create a list that holds the people allocated to this office

        # Create a function that allows you to add allocated people to the list

        # Check if you can still allocate more people

        # Return number of people in the list

        # Return whether the room is still allocatable
