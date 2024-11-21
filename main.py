class MortgageCalculator:
    def __init__(self, principal, annual_rate, years):
        self.principal = principal
        self.monthly_rate = annual_rate / 12 / 100
        self.months = years * 12

    def monthly_payment(self):
        return (self.principal * self.monthly_rate) / (1 - (1 + self.monthly_rate) ** -self.months)