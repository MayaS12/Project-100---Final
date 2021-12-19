class atm:
    def __init__(self, cardNo, pinNo):
        self.cardNo = cardNo
        self.pinNo = pinNo

    def CashWithdrawal(self):
            cash = input("Enter the amount you want to withdraw")
            print("You have withdrawn $", cash, "with the card number:", self.cardNo)
        
    def BalanceEnquiry(self):
            print("You have $500 left on this card:",self.cardNo, "and this pin", self.pinNo)

thing = atm("12365478900", "976902")
thing.CashWithdrawal()
thing.BalanceEnquiry()

        