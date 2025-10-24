#!/usr/bin/python3

class Checkbook:
    """
    Class Description:
        A simple checkbook simulation that allows users to deposit, withdraw, 
        and check their balance.

    Attributes:
        balance (float): The current balance in the checkbook.
    """

    def __init__(self):
        """Initializes the checkbook with a balance of $0.00."""
        self.balance = 0.0

    def deposit(self, amount):
        """
        Function Description:
            Adds a specified amount of money to the checkbook balance.

        Parameters:
            amount (float): The amount to deposit.

        Returns:
            None
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Function Description:
            Withdraws a specified amount from the checkbook balance if sufficient funds exist.

        Parameters:
            amount (float): The amount to withdraw.

        Returns:
            None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Function Description:
            Displays the current checkbook balance.

        Returns:
            None
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Function Description:
        Runs the interactive command-line interface for the Checkbook program.
        Allows the user to deposit, withdraw, view balance, or exit.

    Parameters:
        None

    Returns:
        None
    """
    cb = Checkbook()

    while True:
        action = input("\nWhat would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()

        if action == 'exit':
            print("Goodbye! Thank you for using your checkbook.")
            break

        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                if amount <= 0:
                    print("Please enter a positive amount.")
                else:
                    cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                if amount <= 0:
                    print("Please enter a positive amount.")
                else:
                    cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        elif action == 'balance':
            cb.get_balance()

        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
