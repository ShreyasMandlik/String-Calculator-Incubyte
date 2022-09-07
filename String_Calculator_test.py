import unittest
import String_Calculator


class TestStringCal(unittest.TestCase):
    
    def test_Empty_String(self):
        result=String_Calculator.calculator("")
        self.assertEqual(result,0)
    
    def test_Single_Numeric_String(self):
        result=String_Calculator.calculator("1")
        self.assertEqual(result,1)