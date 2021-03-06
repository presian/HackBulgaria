import sys
import unittest
import os

sys.path.append("..")

from sql_manager import Db
from settings import TEST_DB_NAME


class SqlManagerTests(unittest.TestCase):

    def setUp(self):
        self.sql_manager = Db(TEST_DB_NAME)
        self.sql_manager.create_clients_table()
        self.sql_manager.register('Tester', '123')

    def tearDown(self):
        self.sql_manager.cursor.execute('DROP TABLE clients')

    @classmethod
    def tearDownClass(cls):
        os.remove(TEST_DB_NAME)

    def test_register(self):
        self.sql_manager.register('Dinko', '123123')

        self.sql_manager.cursor.execute(
            'SELECT Count(*)  FROM clients WHERE username = (?) AND password = (?)', ('Dinko', '123123'))
        users_count = self.sql_manager.cursor.fetchone()

        self.assertEqual(users_count[0], 1)

    def test_login(self):
        logged_user = self.sql_manager.login('Tester', '123')
        self.assertEqual(logged_user.get_username(), 'Tester')

    def test_login_wrong_password(self):
        logged_user = self.sql_manager.login('Tester', '123567')
        self.assertFalse(logged_user)

    def test_change_message(self):
        logged_user = self.sql_manager.login('Tester', '123')
        new_message = "podaivinototam"
        self.sql_manager.change_message(new_message, logged_user)
        self.assertEqual(logged_user.get_message(), new_message)

    def test_change_password(self):
        logged_user = self.sql_manager.login('Tester', '123')
        new_password = "12345"
        self.sql_manager.change_pass(new_password, logged_user)

        logged_user_new_password = self.sql_manager.login('Tester', new_password)
        self.assertEqual(logged_user_new_password.get_username(), 'Tester')

if __name__ == '__main__':
    unittest.main()
