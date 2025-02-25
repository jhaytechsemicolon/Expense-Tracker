import unittest
import expenses_tracker

class TestExpensesTracker(unittest.TestCase):
	def test_that_menu_function_exits(self):
		expenses_tracker.get_menu()



	def test_that_expense_function_exits(self):
		expenses_tracker.get_expenses()


	
	def test_that_date_function_exist(self):
		expenses_tracker.get_date('2025','12','04')


	def test_that_date_function_return_valid_date(self):
		actual = expenses_tracker.get_date('0022','12','12')
		result = 'valid input'
		self.assertEqual(actual,result)
	

	def test_that_goods_description_function_exist(self):
		expenses_tracker.get_goods_description('rice')


	def test_that_goods_description_function_collects_valid_input(self):
		actual = expenses_tracker.get_goods_description( "ice cream")
		result = 'valid input'
		self.assertEqual(actual,result)



	def test_that_goods_description_function_returns_null(self):
		actual = expenses_tracker.get_goods_description(" " )
		result = 'valid input'
		self.assertEqual(actual,result)
	

	



	def test_that_amounts_function_exist(self):
		expenses_tracker.get_amounts(123)



	def test_that_amount_function_collects_valid_input(self):
		actual = expenses_tracker.get_amounts(123)
		result = 'valid input'
		self.assertEqual(actual,result)
	



	def test_that_amount_function_returns_null(self):
		actual = expenses_tracker.get_amounts(" ")
		result = 'valid input'
		self.assertEqual(actual,result)
	



	


	def test_that_main_function_exist(self):
		expenses_tracker.main()







	


if __name__ == '__main__':
    unittest.main() 