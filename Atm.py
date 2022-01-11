class Atm(object):
    def __init__(self,atmCardNumber,pinNumber):
        self.atmCardNumber = atmCardNumber
        self.pinNumber = pinNumber

    def CashWithdrawl(self):
        print("cash withdrawl = Rs 100")

    def BalanceEquity(self):
        print("Balance equity")   

hdfcBank = Atm("12344568","12345")
hdfcBank.CashWithdrawl() 
print(hdfcBank.atmCardNumber) 
print(hdfcBank.pinNumber)     