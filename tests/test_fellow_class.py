import unittest

from app.fellow import Fellow
from app.person import Person


class Test_class_Fellow(unittest.TestCase):
    def test_fellow_is_subclass_of_Person(self):
        self.assertTrue(issubclass(Fellow, Person), msg=' Fellow is not a subclass of Person')

    def test_fellow_isinstance_of_class_Fellow(self):
        fellow = Fellow('name', 'position')
        self.assertTrue(isinstance(fellow, Fellow), msg='fellow is not an instance of the Fellow class')

if __name__ == '__main__':
    unittest.main()

