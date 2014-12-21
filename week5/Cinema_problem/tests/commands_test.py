import sys
sys.path.insert(0, '..')
import unittest

from commands import CommandParser


def plus(x, y):
    return x + y


class CommandsTest(unittest.TestCase):

    def setUp(self):
        self.parser = CommandParser()
        
    def test_add_command(self):
        self.parser.add_command('plus', plus)
        self.assertEqual({'plus': plus}, self.parser._CommandParser__commands)

    def test_parse_arguments(self):
        result = self.parser.parse_arguments('(1, 2)')
        # ToDo
                
    def test_execute_key_error(self):
        self.parser.add_command('plus', plus)
        result = self.parser.execute('minus; 3')
        self.assertEqual('No such command', result)

    def test_execute(self):
        self.parser.add_command('plus', plus)
        result = self.parser.execute('plus; (1, 2)')
        self.assertEqual(3, result)
        
if __name__ == '__main__':
    unittest.main()












