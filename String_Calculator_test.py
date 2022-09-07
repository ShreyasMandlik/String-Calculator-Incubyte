import unittest
import String_Calculator


class TestStringCal(unittest.TestCase):
    
    def test_Empty_String(self):
        result=String_Calculator.calculator("")
        self.assertEqual(result,0)
    
    def test_Single_Numeric_String(self):
        result=String_Calculator.calculator("1")
        self.assertEqual(result,1)
    
    def test_two_or_Numeric_having_comma_String(self):
        result=String_Calculator.calculator("1,2")
        self.assertEqual(result,3)

        result1=String_Calculator.calculator("1,2,3,4,5")
        self.assertEqual(result1,15)

    def test_alphabet(self):
        result=String_Calculator.calculator("1,2,a,c")
        self.assertEqual(result,7)
    
    def test_Negative_numbers(self):
            result=String_Calculator.calculator("-123,-4")
            self.assertEqual(result,"Negative Not allowed : -123 ")

