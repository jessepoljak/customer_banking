""" Create a Account class with methods"""

class Account:
    """Creating an Account class with methods"""
    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest

    # This method sets the balance of the account.
    def set_balance(self, balance):
        """Sets the balance for the for the account"""
        self.balance = balance

    # The method sets the interest gained for the account.
    def set_interest(self, interest):
        """Sets the interest gained for the the account"""
        self.interest = interest

    # # The method sets the interest rate for the account.
    # def set_interest_rate(self, interest_rate):
    #     self.interest_rate = interest_rate

    # The method sets the interest earned account.
    def calculate_interest_earned(self, interest_rate, months):
        interest_earned = self.balance * (interest_rate / 100) * (months / 12)
        return interest_earned