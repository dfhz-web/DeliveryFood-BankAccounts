from bank_account import *  #* stands for all


Daniel = BankAccount(1000, "Daniel")
Sara = BankAccount(2000, "Sara")
Manuel = BankAccount(2000, "Manuel")

Daniel.GetBalance()
Sara.GetBalance()
Manuel.GetBalance()

print("Deposit")
Daniel.Deposit(1000)

print('withdraw')
Daniel.WithDraw(10)

print('Transfer')
Daniel.Transfer(1000, Sara)

print('new***************************')

Daniela = InteresRewardsAcct(500,"Daniela")
#Testing methods of the class InteresRewardsAcct that inherit from BankAccount
Daniela.GetBalance()
Daniela.WithDraw(200)
Daniela.Transfer(300,Daniel)
print('**')
Daniela.Deposit(200)
print('**')
Daniela.GetBalance()


print('******SECOND CHILD INHERITANCE***********')
laura = SavingAcct(10, "laura")
laura.WithDraw(5)
laura.Deposit(20)
Daniel.GetBalance()
print('s*********')
laura.Transfer(20, Daniel)
print('s*********')

laura.GetBalance()
Daniel.GetBalance()



# print('*************test***************')
# Daniel.GetBalance()
# laura.GetBalance()
# Daniel.Transfer(1300,laura)
# Daniel.GetBalance()
# laura.GetBalance()

