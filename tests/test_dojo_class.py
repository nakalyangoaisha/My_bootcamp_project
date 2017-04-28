import unittest

from app.dojo import Dojo


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
        self.assertTrue(aisha, msg='Room already exists')

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
        self.assertTrue(k, msg='Object doesnt exist')
        new_people_count = len(self.dojo_instance.people_dict)
        self.assertEqual(new_people_count - initial_people_count, 1)

        k = self.dojo_instance.add_person('kim', 'staff')
        self.assertTrue(k, msg='Person already exists')

    def test_that_staff_are_not_accommodated(self):
        m = self.dojo_instance.add_person('kim', 'staff', 'Yes')
        self.assertEqual(m, 'Staff cannot be accommodated')

    # tests for the allocate room method
    # def test_that_both_name_and_room_type_are_strings(self):
    #     self.assertEqual(self.dojo_instance.add_person(
    #         0, 2), 'Name and room_type should be strings')

    # def tests_that_both_name_room_type_are_not_empty_strings(self):
    #     self.assertEqual(self.dojo_instance.add_person('', ''), 'name and room_type can not be empty')

    def test_that_both_staff_and_fellows_are_allocated_offices(self):
        pass


if __name__ == '__main__':
    unittest.main()
