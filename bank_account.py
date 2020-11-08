# ATM
class Bank_account:
    
    def __init__(self):
        self.balance = 0
        
    def deposit(self, ammount):
        self.balance = self.balance + ammount
        print(self.balance)
        
    def withdraw(self, ammount):
        if self.balance >= ammount:
            self.balance = self.balance - ammount
            print("collect cash")
            print("remaning balance:", self.balance)
        else:
            print("insufficient balance")
        
    def print_balance(self):
        return self.balance
        
account = Bank_account()
for i in range(5):
    print("balance")
    print("deposit")
    print("withdraw")

    user = int(input("enter option:"))
    if user == 1:
        print(account.balance)
    
    elif user == 2:
        account.deposit(int(input("enter amount:")))
    
    elif user == 3:
        account.withdraw(int(input("enter amount:")))
    
    else:
        print("invalid")
    
