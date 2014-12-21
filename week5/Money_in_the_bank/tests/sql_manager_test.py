import sys
import unittest

sys.path.append("..")

import sql_manager


class SqlManagerTests(unittest.TestCase):

    def setUp(self):
        sql_manager.create_clients_table()
        sql_manager.register('Tester', '123Qwerty')

    def tearDown(self):
        sql_manager.cursor.execute('DROP TABLE clients')

    def test_long_pass(self):
        self.assertFalse(sql_manager.long_pass('qwerty'))
        self.assertTrue(sql_manager.long_pass('123456789'))

    def test_have_capital_letter(self):
        self.assertTrue(sql_manager.have_capital_letter('Qwerty'))
        self.assertFalse(sql_manager.have_capital_letter('qweerty'))

    def test_not_contain_username(self):
        self.assertTrue(sql_manager.not_contain_username('Dinko', 'Donko123'))
        self.assertFalse(sql_manager.not_contain_username('Dinko', 'Dinko1234'))
        
    def test_register(self):
        sql_manager.register('Dinko', '123123')
        sql_manager.cursor.execute('SELECT Count(*)  FROM clients WHERE username = (?) AND password = (?)', ('Dinko', '123123'))
        users_count = sql_manager.cursor.fetchone()

        self.assertEqual(users_count[0], 0)

    def test_register_with_strong_pass(self):
        sql_manager.register('Dinko', '123Qwerty')
        sql_manager.cursor.execute('SELECT Count(*)  FROM clients WHERE username = (?) AND password = (?)', ('Dinko', '123Qwerty'))
        users_count = sql_manager.cursor.fetchone()

        self.assertEqual(users_count[0], 1)
        
    def test_login(self):
        logged_user = sql_manager.login('Tester', '123Qwerty')
        self.assertEqual(logged_user.get_username(), 'Tester')

    def test_login_wrong_password(self):
        logged_user = sql_manager.login('Tester', '123')
        self.assertFalse(logged_user)

    def test_change_message(self):
        logged_user = sql_manager.login('Tester', '123Qwerty')
        new_message = "podaivinototam"
        sql_manager.change_message(new_message, logged_user)
        self.assertEqual(logged_user.get_message(), new_message)

    def test_change_password(self):
        logged_user = sql_manager.login('Tester', '123Qwerty')
        new_password = "12345Qwerty"
        sql_manager.change_pass(new_password, logged_user)

        logged_user_new_password = sql_manager.login('Tester', new_password)
        self.assertEqual(logged_user_new_password.get_username(), 'Tester')


if __name__ == '__main__':
    unittest.main()
