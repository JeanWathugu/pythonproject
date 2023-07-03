class BankAccount:
    def __init__(self, accountNumber, holderName, balance=0):
        self.accountNumber= accountNumber
        self.holderName= holderName
        self.balance= balance

    def Depositfunction(self, amount):
        self.balance+= amount
    def Withdraw(self, amount):
        if self.balance>= amount:
            self.balance-= amount
        else:
            print("Insufficient funds")
    def DisplayBalance(self):
        print("ACCOUNT NUMBER:", {self.accountNumber})
        print("HOLDER NAME:" ,{self.holderName})
        print("BALANCE:", {self.balance})

myaccount=BankAccount("1234567", "Phoebe Bridgers", 100)

myaccount.DisplayBalance()
myaccount.Depositfunction(1000)
myaccount.DisplayBalance()
myaccount.Depositfunction(2000)
myaccount.DisplayBalance()
myaccount.Withdraw(5000)














