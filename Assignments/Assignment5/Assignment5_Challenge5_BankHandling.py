class Account:
    def __init__(self,title=None,Balance=0):
        self.title=title
        self.Balance=Balance


    def withdrawal(self, amount):
        if self.Balance >= amount:
            self.Balance=self.Balance-amount
        else:
            print("Do not have enough money in your account")
    def deposit(self, amount):
        self.Balance=amount+self.Balance


    def getBalance(self):
        print('Account Balance is',self.Balance)


class SavingsAccount(Account):
    def __init__(self,title=None,Balance=0,interestRate=0):
        super().__init__(title,Balance)
        self.interestRate=interestRate


    def interestAmount(self):
        interestAmount= (self.interestRate*self.Balance)/100
        print(interestAmount)
#deposit
x=Account('Ashish',2000)
x.deposit(500)
x.getBalance()

#withdrawal
x=Account('Ashish',2000)
x.withdrawal(500)
x.getBalance()

#interestAmount
x=SavingsAccount('Ashish',2000,5)

x.interestAmount()


