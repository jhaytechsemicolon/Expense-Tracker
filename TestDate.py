import unittest
import datefunction

class TestDate(unittest.TestCase):
	def test_that_get_date_function_exist(self):
		datefunction.get_date('date')
	
	def test_that_date_function_collects_valid_input(self):
		actual = datefunction.get_date("2222-22-22")
		result = 'valid input'
		self.assertEqual(actual,result)
		








if __name__ == "__main__":
	unittest.main()