class BalanceException(Exception):  # to work we need line 23 and 32 and below
    pass
 
class Exceptionoutside(Exception):
    pass

class BankAccount:
 
    def __init__(self, initialAmount, accName):
        self.balance = initialAmount  # is an instance variable or a property 
        self.name = accName
        
        print(f"\nAccount '{self.name}'created. \nBalance = ${self.balance:.2f}")

    def GetBalance(self):
        print(f"Account '{self.name}' balance = {self.balance:.2f}")

    def Deposit(self, amount):
        self.balance = self.balance + amount
        print('\nDeposit-completed (parent class)')
        print(f"Account '{self.name}'s been deposited = {self.balance:.2f}")
 
    
    def ViableTransaction(self, amount):
        if self.balance >= amount:
            # self.balance = self.balance - amount
            # print(f"Your new balance ${self.balance}")
        
            return
        else:
            raise BalanceException(
                f"\nSorry, account '{self.name}' \nhas a balance of= {self.balance:.2f}\nInsufficient Funds"
            )
    def WithDraw(self, amount):
        try:
            self.ViableTransaction(amount)
            self.balance -= amount
            print("\nWithdraw completed.(parent)")
            self.GetBalance()
        except BalanceException as error:  #we call the class we created
            print(f'\nWithdraw interrupte: {error}')

    def Transfer(self,amount, account):
        try:
            print("\n*****\n\nLet's start transfer.....")
            self.ViableTransaction(amount)
            self.WithDraw(amount)  # ERROR, IT IS NOT STOPPING, SHOWS THE EXCEPTION AND THEN CONTINUES
            account.Deposit(amount)
            print('\nTransfer completed!')


        except BalanceException as error:  #we call the class we created
            print(f'\nTransfer interrupted: {error}')


class InteresRewardsAcct(BankAccount):
    def __init__(self,  initialAmount, accName):
          super().__init__(initialAmount,accName)

    def Deposit(self, amount):
        amount_percent_included = amount + (amount*0.05)
        self.balance = self.balance + amount_percent_included
        print("\nDeposit completeddddddd.(first-child)")
        self.GetBalance()  #self refers to the object on file project.py
       



class SavingAcct(InteresRewardsAcct):
    def __init__(self,  initialAmount, accName):
        super().__init__(initialAmount, accName)
        self.fee = 5  # for withdraw is gonna be this feed 
    
    #If I want to use the method as it is from the parent class
    # def WithDraw(self, amount):
    #     return super().WithDraw(amount)
       #THIS PART IS IMPORTANT PLEASE 
    def WithDraw(self, amount):
        try:
            self.ViableTransaction(amount + self.fee) # it is taking only one argument
            self.balance = self.balance - (amount + self.fee)
            print('\nWithDraw completed(class second child)')
            self.GetBalance()     
        except Exceptionoutside as error:  #we call the class we created
            print(f'\nWithdraw-interrupted (second-child): {error}')
        

# Solution from blackbox
# class Bank:

#     def WithDraw(self, account, amount):
#         try:
#             account.WithDraw(amount)
#         except BalanceException as error:
#             print(f'\(bankclass)Withdraw interrupte"{error}')


# def WithDraw(self, amount):
#         try:
#             self.ViableTransaction(amount)
#             self.balance -= amount
#             print("\nWithdraw completed.(parent)")
#             self.GetBalance()
#         except BalanceException as error:  #we call the class we created
#             print(f'\nWithdraw interrupte: {error}')