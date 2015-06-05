import unittest
from panda_class import Panda
from panda_error import InvalidEmail


class PandaTest(unittest.TestCase):

    def setUp(self):
        self.test_panda = Panda("Ivo", "ivo@pandamail.com", "male")

    def test_creating_panda(self):
        self.assertTrue(isinstance(self.test_panda, Panda))

    def test_create_new_panda_with_invalid_email(self):
        with self.assertRaises(InvalidEmail):
            Panda("Ivo", "@ivo@pandamail.com", "male")

    def test_name_method(self):
        self.assertEqual(self.test_panda.name(), "Ivo")

    def test_email_method(self):
        self.assertEqual(self.test_panda.email(), "ivo@pandamail.com")

    def test_gender_method(self):
        self.assertEqual(self.test_panda.gender(), "male")

    def test_isMale_method(self):
        self.assertEqual(self.test_panda.isMale(), True)

    def test_isFemale_method(self):
        self.assertEqual(self.test_panda.isFemale(), False)

    def test_eq_dundur(self):
        second_panda = Panda("Ivo", "ivo@pandamail.com", "male")
        self.assertEqual(self.test_panda, second_panda)

    def test_hash(self):
        self.assertTrue(isinstance(hash(self.test_panda), int))

    def test_string_representation(self):
        self.assertEqual(str(self.test_panda), "Name: Ivo\nEmail: ivo@pandamail.com\nGender: male")

    def test_repr_(self):
        self.assertEqual(repr(self.test_panda), "Name: Ivo\nEmail: ivo@pandamail.com\nGender: male")

if __name__ == '__main__':
    unittest.main()
