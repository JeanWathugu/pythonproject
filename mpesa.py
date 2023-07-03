class Mpesatransaction:
    def __init__(self, transactionID, amount):
        self.transactionID = transactionID
        self.amount = amount

    def processTransaction(self):
        raise NotImplementedError("Subclass to use this method")

class DepositTransaction(Mpesatransaction):
    def processTransaction(self):
        print(f"Deposit transaction with ID:", {self.transactionID}, "processed. Amount:", {self.amount})

class WithdrawalTransaction(Mpesatransaction):
    def processTransaction(self):
        print(f"Withdrawal transaction with ID:", {self.transactionID}, "processed. Amount:", {self.amount})

class PaymentTransaction(Mpesatransaction):
    def __init__(self, transactionID, amount, recipient):
        super().__init__(transactionID, amount)
        self.recipient= recipient
    def processTransaction(self):

        print(f"Payment transaction with ID:", {self.transactionID}, "processed. Amount:", {self.amount}, "Recipient:", {self.recipient})

deposit=DepositTransaction("QWEFJR7", "3000")
deposit.processTransaction()

withdrawal = WithdrawalTransaction("HBHRWORY", 400)
withdrawal.processTransaction()

payment = PaymentTransaction("WRYEGBHWE", 500, "Catherine Waithera")
payment.processTransaction()

# create a class called vehicles. Add two properties of your choice. Create subclasses of your choice.eg. motorbike car. Then add more properties within your subclasses.