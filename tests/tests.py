import unittest

from app.dojo import Dojo
from app.room import Room
from app.person import Person
from app.livingspace import Livingspace
from app.office import Office
from app.fellow import Fellow
from app.staff import Staff


class Test_Dojo(unittest.TestCase):
    def setUp(self):
        self.dojo_instance = Dojo()

    # tests for the create_room_method

    def test_returns_error_when_room_name_and_type_are_non_strings(self):
        self.assertEqual(self.dojo_instance.create_room(
            0, 2), 'room_name and room_type should be strings',
            msg='Room name and type must only be strings.')

    def test_create_room_successfully(self):
        # checks if length of the rooms_dict and available rooms was incremented when room is added
        initial_room_count = len(self.dojo_instance.rooms_dict)
        initial_available_rooms_count = len(self.dojo_instance.offices['available'])
        aisha = self.dojo_instance.create_room('a', 'office')
        self.assertTrue(aisha, msg='Object does not exist')
        new_room_count = len(self.dojo_instance.rooms_dict)
        new_available_rooms_count = len(self.dojo_instance.offices['available'])
        self.assertEqual(new_room_count - initial_room_count, 1)
        self.assertEqual(new_available_rooms_count - initial_available_rooms_count, 1)

        # checks that room is only created once
        aisha = self.dojo_instance.create_room('a', 'office')
        self.assertTrue('Room already exists.')

    # tests for the add_person method

    def test_returns_error_when_name_and_position_are_non_strings(self):
        self.assertEqual(self.dojo_instance.add_person(
            0, 2), 'Name and position should be strings',
            msg='Name and position must only be strings.')

    def test_returns_error_when_name_and_position_are_empty_strings(self):
        self.assertEqual(self.dojo_instance.add_person('', ''), 'Name and position can not be empty strings',
                         msg='Name and position must not be empty')

    def test_add_person_successfully(self):
        self.dojo_instance = Dojo()

    def tests_if_length_of_people_dict_increased_when_person_is_added_and_is_only_added_once(self):
        # this also tests that person is added to the people_dict
        initial_people_count = len(self.dojo_instance.people_dict)
        k = self.dojo_instance.add_person('kim', 'staff')
        self.assertTrue(k)
        new_people_count = len(self.dojo_instance.people_dict)
        self.assertEqual(new_people_count - initial_people_count, 1)

        k = self.dojo_instance.add_person('kim', 'staff')
        self.assertTrue('Person already exists.')

    def test_that_staff_are_not_accommodated(self):
        m = self.dojo_instance.add_person('kim', 'staff', 'Yes')
        self.assertEqual(m, 'Staff cannot be accommodated')

    # tests for the allocate room method
    def test_that_both_name_and_room_type_are_strings(self):
        self.assertEqual(self.dojo_instance.add_person(
            0, 2), 'Name and room_type should be strings')

    def tests_that_both_name_room_type_are_not_empty_strings(self):
        self.assertEqual(self.dojo_instance.add_person('', ''), 'name and room_type can not be empty')

    def test_that_both_staff_and_fellows_are_allocated_offices(self):








class Test_class_Person(unittest.TestCase):
    def test_person_is_instance_of_class_Person(self):
        person = Person('name', 'position')
        self.assertTrue(isinstance(person, Person), msg='person is not an instance of the Person class')


class Test_class_Staff(unittest.TestCase):
    def test_staff_is_subclass_of_Person(self):
        self.assertTrue(issubclass(Staff, Person), msg='Staff is not a subclass of Person')

    def test_staff_is_instance_of_class_Staff(self):
        staff = Staff('name', 'position')
        self.assertTrue(isinstance(staff, Staff), msg='staff is not an instance of the Staff class')


class Test_class_Fellow(unittest.TestCase):
    def test_fellow_is_subclass_of_Person(self):
        self.assertTrue(issubclass(Fellow, Person), msg=' Fellow is not a subclass of Person')

    def test_fellow_isinstance_of_class_Fellow(self):
        fellow = Fellow('name', 'position')
        self.assertTrue(isinstance(fellow, Fellow), msg='fellow is not an instance of the Fellow class')


class Test_class_Room(unittest.TestCase):
    def test_if_room_isinstance_of_class_Room(self):
        room = Room('room_name', 'capacity')
        self.assertTrue(isinstance(room, Room), msg='room is not an instance of the Room class')


class Test_class_Office(unittest.TestCase):
    def test_office_is_subclass_of_Room(self):
        self.assertTrue(issubclass(Office, Room), msg='Office is not a subclass of Room')

    def test_office(self):
        office = Office('room_name', 'room_type')
        self.assertTrue(isinstance(office, Office), msg='office is not an instance of the Office class')


class Test_class_Livingspace(unittest.TestCase):
    def test_livingspace_is_subclass_of_Room(self):
        self.assertTrue(issubclass(Livingspace, Room), msg='Livingspace is not a subclass of Room')

    def test_livingspace(self):
        livingspace = Livingspace('room_name', 'capacity', )
        self.assertTrue(isinstance(livingspace, Livingspace),
                        msg='livingspace is not an instance of the Living space class')


if __name__ == '__main__':
    unittest.main()
