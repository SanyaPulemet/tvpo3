from main import *
import unittest


class TestMortgageCalculator(unittest.TestCase):
    def test_monthly_payment_standard(self):
        calculator = MortgageCalculator(100000, 5, 30)
        payment = calculator.monthly_payment()
        self.assertAlmostEqual(payment, 536.82, places=2)

    def test_monthly_payment_high_interest(self):
        calculator = MortgageCalculator(100000, 10, 30)
        payment = calculator.monthly_payment()
        self.assertAlmostEqual(payment, 877.57, places=2)

    def test_monthly_payment_short_term(self):
        calculator = MortgageCalculator(100000, 5, 15)
        payment = calculator.monthly_payment()
        self.assertAlmostEqual(payment, 790.79, places=2)

    def test_monthly_payment_low_principal(self):
        calculator = MortgageCalculator(50000, 5, 30)
        payment = calculator.monthly_payment()
        self.assertAlmostEqual(payment, 268.41, places=2)

    def test_monthly_payment_zero_interest(self):
        calculator = MortgageCalculator(100000, 0, 30)
        payment = calculator.monthly_payment()
        self.assertAlmostEqual(payment, 277.78, places=2)