from abc import ABC, abstractmethod


class Transaction(ABC):

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdrawal(self, amount):
        pass


class BankAccount(ABC):

    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def _set_balance(self, balance):
        self.__balance = balance

    @abstractmethod
    def calculate_interest(self):
        pass

    def display_account_details(self):
        print("Account Number :", self.__account_number)
        print("Balance        :", self.__balance)


class SavingsAccount(BankAccount, Transaction):

    INTEREST_RATE = 4.0

    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount.")
            return

        self._set_balance(self.get_balance() + amount)
        print("Deposit successful.")

    def withdrawal(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
            return

        if amount > self.get_balance():
            print("Insufficient balance.")
            return

        self._set_balance(self.get_balance() - amount)
        print("Withdrawal successful.")

    def calculate_interest(self):
        return (self.get_balance() * self.INTEREST_RATE) / 100


def main():

    print("----- Enter Account Details -----")

    acc_no = int(input("Enter Account Number: "))
    balance = float(input("Enter Initial Balance: "))

    account = SavingsAccount(acc_no, balance)

    while True:

        print("\n----- Banking Menu -----")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Calculate Interest")
        print("4. Display Account Details")
        print("5. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            amt = float(input("Enter deposit amount: "))
            account.deposit(amt)

        elif choice == 2:
            amt = float(input("Enter withdrawal amount: "))
            account.withdrawal(amt)

        elif choice == 3:
            interest = account.calculate_interest()
            print("Interest Amount :", interest)

        elif choice == 4:
            account.display_account_details()

        elif choice == 5:
            print("Thank you for using banking system.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
