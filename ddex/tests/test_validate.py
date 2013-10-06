from DDEXUI.ddex.validate import Validate
import unittest

class ValidateTests(unittest.TestCase):
	def test_upcs_must_only_contain_numbers(self):
		error = Validate().upc("abc123456789")
		self.assertEqual(error, "upc must only contain numbers")

	def test_upcs_cannot_contain_less_than_12_digits(self):
		error = Validate().upc("12345")
		self.assertEqual(error, "upc must be 12 - 13 digit long")

	def test_upcs_cannot_contain_more_than_13_digits(self):
		error = Validate().upc("12345678910235")
		self.assertEqual(error, "upc must be 12 - 13 digit long")

	def test_valid_upcs_do_not_return_errors(self):
		error = Validate().upc("123456789012")
		self.assertEqual(error, None)
