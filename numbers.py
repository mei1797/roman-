import unittest
from roman_numbers import roman_to_decimal

class TestRomanNumbers (unittest.TestCase):
	def test_roman_numbers(self):
		decimal_number=roman_to_decimal('I')
		self.assertEqual(decimal_number, 1)

if __name__=="__main__":
	unittest.main()
