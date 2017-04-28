import unittest

from app.office import Office
from app.room import Room


class Test_class_Office(unittest.TestCase):
    def test_office_is_subclass_of_Room(self):
        self.assertTrue(issubclass(Office, Room), msg='Office is not a subclass of Room')

    def test_office(self):
        office = Office('room_name', 'room_type')
        self.assertTrue(isinstance(office, Office), msg='office is not an instance of the Office class')

if __name__ == '__main__':
    unittest.main()
