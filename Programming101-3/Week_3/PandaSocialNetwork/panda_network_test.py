import unittest
from panda_class import Panda
from panda_network import PandaSocialNetwork
from panda_allready_exist_error import PandaAlreadyThere


class PandaSocialNetworkTest(unittest.TestCase):

    def setUp(self):
        self.__ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        self.__rado = Panda("rado", "rado@pandamail.com", "male")
        self.__pandabook = PandaSocialNetwork()
        self.__full_pandabook = PandaSocialNetwork()
        self.__full_pandabook.add_panda(self.__rado)
        self.__full_pandabook.add_panda(self.__ivo)
        self.__full_pandabook.make_friends(self.__ivo, self.__rado)
        self.__full_pandabook

    def test_get_panda_list_method(self):
        self.assertDictEqual(self.__pandabook.get_panda_list(), {})

    def test_add_panda(self):
        self.__pandabook.add_panda(self.__ivo)
        self.assertDictEqual(self.__pandabook.get_panda_list(), {self.__ivo: []})

    def test_add_panda_with_duplicate_panda(self):
        with self.assertRaises(PandaAlreadyThere):
            self.__full_pandabook.add_panda(self.__ivo)

    def test_has_panda(self):
        self.assertTrue(self.__full_pandabook.has_panda(self.__rado))

    def test_make_friends_method_for_first_panda(self):
        self.assertEqual(self.__full_pandabook.get_panda_list()[self.__ivo], [self.__rado])

    def test_make_friends_method_for_second_panda(self):
        self.assertEqual(self.__full_pandabook.get_panda_list()[self.__rado], [self.__ivo])

    def test_are_friends(self):
        self.assertTrue(self.__full_pandabook.are_friends(self.__ivo, self.__rado))

    def test_friends_of(self):
        self.assertListEqual(self.__full_pandabook.friends_of(self.__ivo), [self.__rado])

    def test_friends_of_with_unexisting_panda(self):
        new_panda = Panda("New", "new@pandamail.com", "female")
        self.assertFalse(self.__full_pandabook.friends_of(new_panda), [self.__rado])

    def test_connection_level(self):
        self.assertEqual(self.__full_pandabook.connection_level(self.__ivo, self.__rado), 1)

    def test_connection_level_with_unexisting_panda(self):
        new_panda = Panda("New", "new@pandamail.com", "female")
        self.assertEqual(self.__full_pandabook.connection_level(self.__ivo, new_panda), -1)

    def test_connection_level_with_third_panda_without_relations(self):
        new_panda = Panda("New", "new@pandamail.com", "female")
        self.__full_pandabook.add_panda(new_panda)
        self.assertEqual(self.__full_pandabook.connection_level(self.__ivo, new_panda), -1)

    # def test_connection_level_with_third_panda(self):
    #     new_panda = Panda("New", "new@pandamail.com", "female")
    #     self.__full_pandabook.add_panda(new_panda)
    #     self.__full_pandabook.make_friends(self.__ivo, new_panda)
    #     print("a")
    #     self.assertEqual(self.__full_pandabook.connection_level(self.__rado, new_panda), 2)

if __name__ == '__main__':
    unittest.main()
