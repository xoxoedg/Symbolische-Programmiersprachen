from account_type import AccountType
"""Exercise 1: Bank account class [5 points]

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
    Represents a bank account with basic operations like
    deposit, withdraw, and applying interest rates.

    Attributes:
        holder (str): Name of the account holder.
        balance (float): Current balance in the account.
        account_type (AccountType): Type of the account.
    """

    def __str__(self):
        return (
            f"----- Account Info -----\n"
            f"Holder: {self.holder}\n"
            f"Balance: {self.balance:.2f} €\n"
            f"Type: {self.account_type.name}\n"
            f"-------------------------"
        )

    def __init__(self, acc_id, holder, balance=0, account_type=AccountType.STANDARD):
        self.isAuthorized = False
        self.pin = 1111
        self.id = acc_id
        self.holder = holder
        self.account_type = account_type
        self.balance = balance




    def authorize(self, pin):
        """
        Authorize with account pin

       Parameters:
           pin (int): Pin of the account

       Returns:
           None
       """
        if self.pin == pin:
            self.isAuthorized = True

    def deposit(self, amount):
        if not self.isAuthorized:
            print("You need to enter your pin first")

        if amount < 0:
            print("Sorry you can deposit a negative amount")
        else:
            self.balance += amount

        self.isAuthorized = False


    def withdraw(self, amount):
            new_balance = self.balance - amount
            if not self.isAuthorized:
                print("You need to enter your pin first")

            if new_balance < 0:
                print("You cant deposit. Because youre balance would be negative")
            else:
                self.balance -= amount
            self.isAuthorized = False
            return amount

    def apply_interest(self):
        match self.account_type:
            case AccountType.STANDARD:
                self.balance += self.balance * 1.2
            case AccountType.GOLD:
                self.balance += self.balance * 1.7
            case AccountType.PLATINUM:
                self.balance += self.balance * 2.2





if __name__ == "__main__":
    print("Welcome to the Python Bank!")
    alice_account = Account(15, "alice", 300, AccountType.PLATINUM)
    alice_account.authorize(1111)
    alice_account.withdraw(30)
