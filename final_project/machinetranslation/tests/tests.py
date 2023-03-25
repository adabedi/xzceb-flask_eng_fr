import sys
import unittest

sys.path.append('../')
from ..machinetranslation.translator import english_to_french, french_to_english

GREETING_ENG = 'Hello'
GRETTING_FR = 'Bonjour'

class TestTranslator(unittest.TestCase):

    def test_english_to_french(self):
        self.assertIsNone(english_to_french(None))
        self.assertEqual(english_to_french(GREETING_ENG),GRETTING_FR)

    def test_french_to_english(self):
        self.assertIsNone(english_to_french(None))
        self.assertEqual(french_to_english(GRETTING_FR),GREETING_ENG)

if __name__ == '__main__':
    unittest.main()
