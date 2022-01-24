import unittest
from unittest.mock import patch
import a1 as my


class TestGetRegularInput(unittest.TestCase):
	@patch('a1.input', create=True)
	def test_1(self, user_input):
		user_input.side_effect = ['0 1 1 3 4 8 1 8']
		user_output = my.get_regular_input()
		exp_output = [1, 3, 0, 1, 1, 0, 0, 0, 2, 0]
		self.assertEqual(exp_output, user_output)


class TestCalculateCategoryWiseCost(unittest.TestCase):
	def test_1(self):
		quantities = [1, 3, 0, 1, 1, 0, 0, 0, 2, 0]
		user_output = my.calculate_category_wise_cost(quantities)
		exp_output = (2300, 50000, 200)
		self.assertEqual(exp_output, user_output)


class TestCalculateDiscountedPrices(unittest.TestCase):
	def test_1(self):
		costs = (2300, 50000, 200)
		user_output = my.calculate_discounted_prices(*costs)
		exp_output = (2070, 45000, 200)
		self.assertEqual(exp_output, user_output)


class TestGetTax(unittest.TestCase):
	def test_1(self):
		costs = (2070, 45000, 200)
		user_output = my.calculate_tax(*costs)
		exp_output = (54237, 6967)
		self.assertEqual(exp_output, user_output)


class TestApplyCouponCode(unittest.TestCase):
	@patch('a1.input', create=True)
	def test_1(self, user_input):
		total_cost = 54237
		user_input.side_effect = [
			'ABCD99',
			''
		]

		user_output = my.apply_coupon_code(total_cost)
		exp_output = (54237, 0)
		self.assertEqual(exp_output, user_output)


if __name__ == '__main__':
	unittest.main()
