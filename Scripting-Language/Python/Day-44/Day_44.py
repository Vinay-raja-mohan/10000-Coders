import random
from abc import ABC, abstractmethod

class Bank(ABC):

    @abstractmethod
    def create_acc(self):
        pass

    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass

    @abstractmethod
    def check_balance(self):
        pass


class SBI(Bank):

    def __init__(self):
        self.__accounts = {}   
        self.ifsc = "SBIN0001234"

    def generate_account_number(self):
        while True:
            acc_no = random.randint(1000000000, 9999999999)
            if acc_no not in self.__accounts:
                return acc_no

    def create_acc(self):
        print("----- Create Bank Account -----")

        name = input("Enter Name: ")
        mobile = input("Enter Mobile Number: ")
        aadhar = input("Enter Aadhaar Number: ")

        print("\n1. Savings Account")
        print("2. Current Account")

        choice = input("Enter choice: ")

        if not choice.isdigit():
            print("Invalid input!")
            return

        choice = int(choice)
        acc_no = self.generate_account_number()

        if choice == 1:
            acc_type = "Savings"
            min_deposit = 1000
        elif choice == 2:
            acc_type = "Current"
            min_deposit = 500
        else:
            print("Invalid choice")
            return

        deposit = input(f"Deposit minimum ₹{min_deposit}: ")

        if not deposit.isdigit():
            print("Invalid amount!")
            return

        deposit = int(deposit)

        if deposit < min_deposit:
            print("Minimum balance not maintained.")
            return

        self.__accounts[acc_no] = {
            "Name": name,
            "Balance": deposit,
            "Type": acc_type,
            "IFSC": self.ifsc,
            "Mobile": mobile,
            "Aadhar": aadhar
        }

        print(f"Account created successfully! Account No: {acc_no}")

    def deposit(self):
        acc_no = input("Enter Account Number: ")
        amount = input("Enter amount to deposit: ")

        if not acc_no.isdigit() or not amount.isdigit():
            print("Invalid input!")
            return

        acc_no = int(acc_no)
        amount = int(amount)

        if amount <= 0:
            print("Enter valid amount!")
            return

        if acc_no in self.__accounts:
            self.__accounts[acc_no]["Balance"] += amount
            print("Amount deposited successfully.")
        else:
            print("Account not found!")

    def withdraw(self):
        acc_no = input("Enter Account Number: ")
        amount = input("Enter amount to withdraw: ")

        if not acc_no.isdigit() or not amount.isdigit():
            print("Invalid input!")
            return

        acc_no = int(acc_no)
        amount = int(amount)

        if amount <= 0:
            print("Enter valid amount!")
            return

        if acc_no in self.__accounts:
            balance = self.__accounts[acc_no]["Balance"]
            acc_type = self.__accounts[acc_no]["Type"]

            if acc_type == "Savings" and (balance - amount) < 1000:
                print("Minimum balance violation!")
                return

            if balance >= amount:
                self.__accounts[acc_no]["Balance"] -= amount
                print("Withdrawal successful.")
            else:
                print("Insufficient balance!")
        else:
            print("Account not found!")

    def check_balance(self):
        acc_no = input("Enter Account Number: ")

        if not acc_no.isdigit():
            print("Invalid input!")
            return

        acc_no = int(acc_no)

        if acc_no in self.__accounts:
            print("Balance:", self.__accounts[acc_no]["Balance"])
        else:
            print("Account not found!")

    def display_accounts(self):
        print("\n----- All Accounts -----")
        for acc_no, details in self.__accounts.items():
            print(f"\nAccount No: {acc_no}")
            for k, v in details.items():
                print(f"{k}: {v}")


bank = SBI()

while True:
    print("\n1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Display Accounts")
    print("6. Exit")

    ch = input("Enter choice: ")

    if not ch.isdigit():
        print("Enter numbers only!")
        continue

    ch = int(ch)

    if ch == 1:
        bank.create_acc()
    elif ch == 2:
        bank.deposit()
    elif ch == 3:
        bank.withdraw()
    elif ch == 4:
        bank.check_balance()
    elif ch == 5:
        bank.display_accounts()
    elif ch == 6:
        print("Exiting...")
        break
    else:
        print("Invalid choice!")