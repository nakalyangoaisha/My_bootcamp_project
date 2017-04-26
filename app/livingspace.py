from app.room import Room


class Livingspace(Room):
    def __init__(self, room_name, capacity, room_type):
        super().__init__(room_name, capacity, room_type)
        capacity = 4
        room_type = 'Livingspace'
