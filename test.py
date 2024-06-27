import unittest
from main import getNewWord
from main import getDefintion
from words import word_list
# from main import something we do not have a class to import?

# consts
EXPCTED_DEF = 'the same throughout in structure or composition'


# Test Ideas:
# Test getDefintion by using a word and anticapte an expected definition
class Test(unittest.TestCase):
    def test_definition(self):
        self.assertEqual(getDefintion('consistent'), 'EXPCTED_DEF')

# Test getNewWord by comparing function against itself and expect not equal

    def test_word_getter(self):
        temp = getNewWord(word_list)
        self.assertTrue(temp.isalpha())
