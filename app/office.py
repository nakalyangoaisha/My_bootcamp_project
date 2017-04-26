from app.room import Room


class Office(Room):
    def __init__(self, room_name):
        capacity = 6
        room_type = 'Office'
        Room.__init__(self, room_name, capacity, room_type)
