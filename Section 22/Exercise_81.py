class BankAccount:
    def __init__(self, account_holder, initial_balance):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("With drawl amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount

    def transfer(self, target_account, amount):
        if amount <= 0:
            print("Transfer amount must be positive")
        elif amount > self.balance:
            print("Insufficient balance for transferring funds")
        else:
            self.balance -= amount
            target_account.balance += amount
            return target_account.balance


acc1 = BankAccount("John Doe", 1000)
acc2 = BankAccount("Jane Smith", 2000)

assert acc1.balance == 1000
assert acc2.balance == 2000

acc1.deposit(500)
acc2.withdraw(100)
# print(acc1.transfer(acc2, 200))
acc1.transfer(acc2, 200)

# assert acc1.balance == 1300
# assert acc2.balance == 2300
# print("Hi Bangaram")

acc3 = BankAccount("Alice Johnson", 500)
acc4 = BankAccount("Bob Brown", 1500)

assert acc3.balance == 500
assert acc4.balance == 1500

acc3.deposit(100)
acc4.withdraw(200)
acc3.transfer(acc4, 300)
# print(acc3.transfer(acc4, 300))
assert acc3.balance == 300
assert acc4.balance == 1600
