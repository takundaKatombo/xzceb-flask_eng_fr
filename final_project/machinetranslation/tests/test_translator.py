import unittest

from translator import english_to_french,french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(english_to_french('hello, how are you'),'bonjour, sa va')
        self.assertNotEqual(english_to_french('hi,my name is'),'bonjour, sa va')


class TestFrenchToEnglish(unittest.TestCase):
    def test_frenchToEnglish(self):
        self.assertEqual(french_to_english('bonjour'),'hello')
        self.assertNotEqual(french_to_english('sa va'),'thats not true')

unittest.main
