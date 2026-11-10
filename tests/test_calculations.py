import unittest

from finscope.calculations import (
    compound_interest,
    inflation_adjusted_value,
    investment_return,
    simple_interest,
)


class TestCalculations(unittest.TestCase):
    def test_simple_interest(self):
        self.assertAlmostEqual(simple_interest(1000, 5, 2), 100)

    def test_compound_interest_annual(self):
        self.assertAlmostEqual(compound_interest(1000, 10, 2), 1210)

    def test_compound_interest_monthly(self):
        self.assertGreater(compound_interest(1000, 10, 1, 12), 1100)

    def test_investment_return_gain(self):
        self.assertAlmostEqual(investment_return(100, 125), 25)

    def test_investment_return_loss(self):
        self.assertAlmostEqual(investment_return(100, 80), -20)

    def test_zero_initial_investment(self):
        self.assertIsNone(investment_return(0, 100))

    def test_inflation(self):
        self.assertAlmostEqual(inflation_adjusted_value(100, 10, 2), 121)

    def test_negative_input_rejected(self):
        with self.assertRaises(ValueError):
            simple_interest(-1, 5, 2)

    def test_invalid_compounding_frequency(self):
        with self.assertRaises(ValueError):
            compound_interest(100, 5, 2, 0)


if __name__ == "__main__":
    unittest.main()
