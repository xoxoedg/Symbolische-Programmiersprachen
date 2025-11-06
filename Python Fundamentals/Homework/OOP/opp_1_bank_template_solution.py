"""
Exercise 1: Bank account class [5 points]

1. Complete Account class with docstrings** [1 point]
    - Properly defined Account class with correct attributes and methods.
    - Every method has a documentation string that describes its functionality.

2. Main application with various accounts** [1 point]
    - Successfully creates multiple account instances.
    - Demonstrates depositing and withdrawing money on those accounts.
    - Changes the account holder of an account using a setter method.

3. Modified withdraw function** [1 point]
    - Ensures that the account balance never drops below -500.
    - If withdrawal would result in a balance less than -500, prints an appropriate error message and does not allow the withdrawal.

4. Implement apply_interest() function** [1 point]
    - Allows account holders to choose between 3 different types of accounts and applies the correct interest rate for each account type.
    - Correctly updates the balance based on the interest rate.
    - Interest rates:
        - Standard Account: 1.2%
        - Gold Account: 1.7%
        - Platinum Account: 2.2%

5. Implement the __str__ magic method** [1 point]
    - Returns a string with the account holder's name.
    - Includes the current balance in the string.
    - States the account type in the string.
"""


class Account:
    """
    A class to represent a banking account.

    Attributes
    ----------
    number : int
        unique id for the account
    balance : float
        starting balance of the banking account
    holder: str
        person to whom the account belongs
    account_type: str
        type of the account (Standard Account, Gold Account, Platinum Account)

    Methods
    -------
    withdraw(amount):
        Withdraw an amount of money from the banking account.
    deposit(amount):
        Deposit an amount in the banking account.
    set_account_holder(name):
        Change the name of the account holder.
    apply_interest():
        Apply the respective interest rate to the current balance.
    """

    def __init__(self, num, person, account_type="Standard Account"):
        self.number = num
        self._holder = person
        self.balance = 0.0
        self.account_type = account_type

    def __str__(self):
        return (f"###Account information###\n"
                f"Account ID: {self.number}\n"
                f"Holder of the account: {self.holder}\n"
                f"Current balance: ${self.balance:.2f}\n"
                f"Account type: {self.account_type}")

    @property
    def holder(self):
        return self._holder

    @holder.setter
    def holder(self, person):
        self._holder = person

    def deposit(self, amount):
        """Deposit an amount into the banking account."""
        print(f"Depositing ${amount}...")
        self.balance += amount

    def withdraw(self, amount):
        """Withdraw an amount from the banking account if it doesn't exceed the overdraft limit."""
        print(f"Withdrawing ${amount}...")
        if self.balance - amount < -500:
            print("Your balance cannot be lower than -500.")
        else:
            self.balance -= amount

    def apply_interest(self):
        """Apply the respective interest rate based on the account type."""
        rates = {
            "Standard Account": 1.012,   # 1.2%
            "Gold Account": 1.017,       # 1.7%
            "Platinum Account": 1.022    # 2.2%
        }
        print(f"Applying interest for {self.account_type} ...")
        rate = rates.get(self.account_type, 1)
        self.balance *= rate


if __name__ == "__main__":
    print("Welcome to the Python Bank!")
    katAcc = Account(1, "Katerina", "Gold Account")
    anneAcc = Account(2, "Anne", "Platinum Account")
    katAcc.deposit(500)
    anneAcc.deposit(100000)
    print(katAcc)
    print(anneAcc)
    katAcc.withdraw(10000)
    anneAcc.withdraw(100)
    katAcc.apply_interest()
    print(katAcc)
    anneAcc.holder = "Mary"
    print(anneAcc)
