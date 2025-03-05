class Bank:
    def __init__(self, customerName, accountNo, balance):
        self.name = customerName
        self.accountNo = accountNo
        self.balance = balance


    def __str__(self):
        return f"{self.name}({self.accountNo},{self.balance})"
    
Bank1 = Bank("John", 123456, 1000)
print(Bank1)