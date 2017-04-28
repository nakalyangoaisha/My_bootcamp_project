import unittest

from app.room import Room
from app.livingspace import Livingspace


class Test_class_Livingspace(unittest.TestCase):
    def test_livingspace_is_subclass_of_Room(self):
        self.assertTrue(issubclass(Livingspace, Room), msg='Livingspace is not a subclass of Room')

    def test_livingspace(self):
        livingspace = Livingspace('room_name', 'capacity', )
        self.assertTrue(isinstance(livingspace, Livingspace),
                        msg='livingspace is not an instance of the Living space class')

if __name__ == '__main__':
    unittest.main()
