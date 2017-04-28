import unittest

from app.room import Room


class Test_class_Room(unittest.TestCase):
    def test_if_room_isinstance_of_class_Room(self):
        room = Room('room_name', 'capacity')
        self.assertTrue(isinstance(room, Room), msg='room is not an instance of the Room class')

if __name__ == '__main__':
    unittest.main()
