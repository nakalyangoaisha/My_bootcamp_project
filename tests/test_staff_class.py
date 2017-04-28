import unittest

from app.staff import Staff
from app.person import Person


class Test_class_Staff(unittest.TestCase):
    def test_staff_is_subclass_of_Person(self):
        self.assertTrue(issubclass(Staff, Person), msg='Staff is not a subclass of Person')

    def test_staff_is_instance_of_class_Staff(self):
        staff = Staff('name', 'position')
        self.assertTrue(isinstance(staff, Staff), msg='staff is not an instance of the Staff class')

if __name__ == '__main__':
    unittest.main()
