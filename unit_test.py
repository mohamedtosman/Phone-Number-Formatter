import unittest 
from PhoneNumberFormatter import PhoneNumberFormatter

class TestPhoneNumberFormatter(unittest.TestCase): 
    
    def setUp(self):
        self.formatter = PhoneNumberFormatter()
        self.UKFormatter = self.formatter.UK()

    def test_successful_07_case(self):
        """
        Test correct number starting with 07
        """
        self.assertEqual(self.UKFormatter.format("07123456789"), "+447123456789")

    def test_successful_44_case(self):
        """
        Test correct number starting with 447
        """
        self.assertEqual(self.UKFormatter.format("447123456789"), "+447123456789")

    def test_successful_plus44_case(self):
        """
        Test correct number starting with +447
        """
        self.assertEqual(self.UKFormatter.format("+447123456789"), "+447123456789")

    def test_successful_whitespace_case(self):
        """
        Test correct number starting with white spaces in between
        """
        self.assertEqual(self.UKFormatter.format("+4471234  56789"), "+447123456789")

    def test_invalid_number(self):
        """
        Test number with incorrect prefix
        """
        self.assertEqual(self.UKFormatter.format("0634343"), "Invalid number.")

    def test_less_than_nine_digits_case(self):
        """
        Test number starting with correct prefix but with less than 9 digits
        """
        self.assertEqual(self.UKFormatter.format("07123456"), "Invalid number.")

    def test_more_than_nine_digits_case(self):
        """
        Test number starting with correct prefix but with more than 9 digits
        """
        self.assertEqual(self.UKFormatter.format("071234567899"), "Invalid number.")

    def test_not_a_number_case(self):
        """
        Test inputting a value that is not a number
        """
        self.assertEqual(self.UKFormatter.format("Not a number"), "Invalid number.")

    def test_numbers_and_characters(self):
        """
        Test number with a character in it
        """
        self.assertEqual(self.UKFormatter.format("+4471234 k6789"), "Invalid number.")

  
if __name__ == '__main__': 
    unittest.main()
