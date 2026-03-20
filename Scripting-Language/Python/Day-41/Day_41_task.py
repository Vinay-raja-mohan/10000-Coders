import random

class Bank:
    def __init__(self):
        self.accounts = {}   
        self.ifsc = "SBIN0001234" 

    def generate_account_number(self):
        return random.randint(1000000000, 9999999999)

    def create_acc(self):
        print("----- Create Bank Account -----")

        name = input("Enter Name: ")
        mobile = input("Enter Mobile Number: ")
        aadhar = input("Enter Aadhaar Number: ")

        print("\nSelect Account Type:")
        print("1. Savings Account")
        print("2. Current Account")

        choice = int(input("Enter choice (1/2): "))

        acc_no = self.generate_account_number()

        if choice == 1:
            acc_type = "Savings"
            min_deposit = 1000
        elif choice == 2:
            acc_type = "Current"
            min_deposit = 500
        else:
            print("Invalid choice ")
            return

        deposit = int(input(f"Deposit minimum ₹{min_deposit}: "))

        if deposit < min_deposit:
            print("Minimum balance not maintained. Account not created.")
            return

        # Store in dictionary
        self.accounts[acc_no] = {
            "Name": name,
            "Mobile": mobile,
            "Aadhar": aadhar,
            "IFSC": self.ifsc,
            "Account Type": acc_type,
            "Balance": deposit
        }

        print("\n Account Created Successfully!")
        print("Account Number:", acc_no)

    def display_accounts(self):
        print("\n----- All Accounts -----")
        for acc_no, details in self.accounts.items():
            print(f"\nAccount No: {acc_no}")
            for key, value in details.items():
                print(f"{key}: {value}")


bank = Bank()

while True:
    print("\n1. Create Account")
    print("2. Display Accounts")
    print("3. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        bank.create_acc()
    elif ch == 2:
        bank.display_accounts()
    elif ch == 3:
        print("Exiting...")
        break
    else:
        print("Invalid choice!")