import unittest
from random import Random
from unittest import TestCase

from app.dojo import Dojo, Dojo_instance
from app.room import Room
from app.person import Person
from app.livingspace import Livingspace
from app.office import Office
from app.fellow import Fellow
from app.staff import Staff


class Test_ClassRelationships(TestCase):
    def test_office_is_subclass_of_Room(self):
        self.assertTrue(issubclass(Office, Room), msg='Office is not a subclass of Room')

    def test_livingspace_is_subclass_of_Room(self):
        self.assertTrue(issubclass(Livingspace, Room), msg='Livingspace is not a subclass of Room')

    def test_fellow_is_subclass_of_Person(self):
        self.assertTrue(issubclass(Fellow, Person), msg=' Fellow is not a subclass of Person')

    def test_staff_is_subclass_of_Person(self):
        self.assertTrue(issubclass(Staff, Person), msg='Staff is not a subclass of Person')


class TestClasses(unittest.TestCase):
    def setUp(self):
        self.Dojo_instance = Dojo()
        global random

    def test_office(self):
        office = Office('room_name')
        self.assertTrue(isinstance(office, Office), msg='office is not an instance of the Office class')

    def test_livingspace(self):
        livingspace = Livingspace('room_name', 'capacity', 'room_type')
        self.assertTrue(isinstance(livingspace, Livingspace),
                        msg='livingspace is not an instance of the Living space class')

    def test_staff(self):
        staff = Staff('name', 'position')
        self.assertTrue(isinstance(staff, Staff), msg='staff is not an instance of the Staff class')

    def test_fellow(self):
        fellow = Fellow('name', 'position')
        self.assertTrue(isinstance(fellow, Fellow), msg='fellow is not an instance of the Fellow')

    def test_create_room_successfully(self,):
        initial_room_count = len(self.Dojo_instance.room_list)
        a_office = Dojo_instance.create_room('a', 'office')
        self.assertTrue(a_office)
        new_room_count = len(Dojo_instance.room_list)
        self.assertEqual(new_room_count - initial_room_count, 1)

        b_livingspace = Dojo_instance.create_room('b', 'livingspace')
        self.assertTrue(b_livingspace)
        new_room_count = len(Dojo_instance.room_list)
        self.assertEqual(new_room_count - initial_room_count, 2)

    def test_add_person_successfully(self):
        initial_people_count = len(Dojo_instance.people_list)
        aisha_fellow = Dojo_instance.add_person('aisha', 'fellow')
        self.assertTrue(aisha_fellow)
        new_people_count = len(Dojo_instance.people_list)
        self.assertEqual(new_people_count - initial_people_count, 1)

        noor_staff = Dojo_instance.add_person('noor', 'staff')
        self.assertTrue(noor_staff)
        new_people_count = len(Dojo_instance.people_list)
        self.assertEqual(new_people_count - initial_people_count, 2)









if __name__ == '__main__':
    unittest.main()
