import threading

class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        self.lock = threading.Lock()

    def deposit(self, amount):
        with self.lock:
            self.balance += amount
            print(f"Deposited {amount}, New Balance: {self.balance}")

    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew {amount}, New Balance: {self.balance}")
            else:
                print(f"Failed Withdrawal: Insufficient funds for {amount}")

# Create a shared bank account
account = BankAccount(100)

def client_transactions():
    for _ in range(5):
        account.deposit(10)
        account.withdraw(5)

# Create client threads
threads = [threading.Thread(target=client_transactions) for _ in range(5)]

# Start threads
for thread in threads:
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print(f"Final account balance: {account.balance}")
