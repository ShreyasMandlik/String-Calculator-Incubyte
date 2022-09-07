import unittest
import String_Calculator


class TestStringCal(unittest.TestCase):
    
    def test_Empty_String(self):
        result=String_Calculator.calculator("")
        self.assertEqual(result,0)