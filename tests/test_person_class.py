import unittest

from app.person import Person


class Test_class_Person(unittest.TestCase):
    def test_person_is_instance_of_class_Person(self):
        person = Person('name', 'position')
        self.assertTrue(isinstance(person, Person), msg='person is not an instance of the Person class')

if __name__ == '__main__':
    unittest.main()
