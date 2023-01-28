import itertools


# class BankAccount
class BankAccount:
    # create a auto-increasing number using itertools
    account_number = itertools.count(100000)

    # constructor
    def __init__(self, first_name, last_name, balance):
        self.account_number = next(BankAccount.account_number)
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance

    # method to add a new bank account
    def add_account(self):
        self.account_number = next(BankAccount.account_number)
        self.first_name = input("Enter the first name: ")
        self.last_name = input("Enter the last name: ")
        self.balance = int(input("Enter the balance: "))

        # check if the balance is a positive number
        if self.balance < 0:
            print("The balance must be a positive number")
            return

    # method to update a bank account by account number
    def update_account(self, account_number):
        # check if the account number exists
        if self.account_number == account_number:
            self.first_name = input("Enter the first name: ")
            self.last_name = input("Enter the last name: ")
            self.balance = int(input("Enter the balance: "))

            # check if the balance is a positive number
            if self.balance < 0:
                print("The balance must be a positive number")
                return
            # if the balance is a positive number, update the bank account
            else:
                print("The bank account has been updated")
                return
        else:
            print("The account number does not exist")
            return

    # method to delete a bank account by account number
    def delete_account(self, account_number):
        # check if the account number exists
        if self.account_number == account_number:
            self.account_number = ""
            self.first_name = ""
            self.last_name = ""
            self.balance = 0
            print("The bank account has been deleted")
            return
        else:
            print("The account number does not exist")
            return

    # method to add money to a bank account
    def deposit(self, account_number, amount):
        # check if the account number exists
        if self.account_number == account_number:
            self.balance += amount
            print("The new balance is: ", self.balance)
            return
        else:
            print("The account number does not exist")
            return

    # method to withdraw money from a bank account
    def withdraw(self, account_number, amount):
        # check if the account number exists
        if self.account_number == account_number:
            # check if the balance is greater than the amount
            if self.balance > amount:
                self.balance -= amount
                print("The new balance is: ", self.balance)
                return
            else:
                print("The balance is not enough")
                return
        else:
            print("The account number does not exist")
            return

    # method to transfer money from an account to an account
    def transfer(self, from_account_number, to_account_number, amount):
        # check if the from account number exists
        if self.account_number == from_account_number:
            # check if the balance is greater than the amount
            if self.balance > amount:
                self.balance -= amount
                print("The new balance is: ", self.balance)
                # check if the to account number exists
                if self.account_number == to_account_number:
                    self.balance += amount
                    print("The new balance is: ", self.balance)
                    return
                else:
                    print("The to account number does not exist")
                    return
            else:
                print("The balance is not enough")
                return
        else:
            print("The from account number does not exist")
            return

    # method to find bank accounts by a first name
    def find_by_first_name(self, first_name):
        # check if the first name exists
        if self.first_name == first_name:
            print("The account number is: ", self.account_number)
            print("The first name is: ", self.first_name)
            print("The last name is: ", self.last_name)
            print("The balance is: ", self.balance)
            return
        else:
            print("The first name does not exist")
            return

    # method to sort bank accounts by the last name
    def sort_by_last_name(self):
        print("The account number is: ", self.account_number)
        print("The first name is: ", self.first_name)
        print("The last name is: ", self.last_name)
        print("The balance is: ", self.balance)
        return

    # method to return bank accounts that have a balance greater than a given amount
    def filter_by_balance(self, amount):
        # check if the balance is greater than the given amount
        if self.balance > amount:
            print("The account number is: ", self.account_number)
            print("The first name is: ", self.first_name)
            print("The last name is: ", self.last_name)
            print("The balance is: ", self.balance)
            return
        else:
            print("The balance is not enough")
            return

    # print all bank accounts
    def print_bank_accounts(self):
        for i in range(len(self.account_number)):
            print("The account number is: ", self.account_number)
            print("The first name is: ", self.first_name)
            print("The last name is: ", self.last_name)
            print("The balance is: ", self.balance)
            return


# call the fuctions
bank_account1 = BankAccount("Leonardo", "Aureliano", 9999)
bank_account2 = BankAccount("Leonel", "Messi", 1234)
bank_account3 = BankAccount("Ayrton", "Senna", 0000)
bank_account3.add_account()
bank_account4 = BankAccount("Cristiano", "Ronaldo", 5678)
bank_account1.update_account(100001)
bank_account1.delete_account(100001)
bank_account1.deposit(100002, 100)
bank_account1.withdraw(100002, 100)
bank_account1.transfer(100002, 100003, 100)
bank_account1.find_by_first_name("Leonardo")
bank_account1.sort_by_last_name()
bank_account1.filter_by_balance(100)





