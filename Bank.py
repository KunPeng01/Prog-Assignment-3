
# define class account and methond 
class Account:
    def __init__(self,accountNumber, accountHolderName, rateOfinterest, currentchecquingbalance, currentsavingbalance):
        self.accountNumber = accountNumber
        self.accountHolderName = accountHolderName
        self.rateOfinterest = rateOfinterest
        self.currentchecquingbalance = currentchecquingbalance
        self.currentsavingbalance  = currentsavingbalance

    def getAccountNumber(self):
        return self.accountNumber

    def getAccountHolderName(self):
        return self.accountHolderName

    def getRateOfinterest(self):
        return self.rateOfinterest

    def getCurrentChecquingBalance(self):
        return self.currentchecquingbalance

    def getCurrentSavingBalance(self):
        return self.currentsavingbalance

    def SavingDeposit(self,amount):
        self.currentsavingbalance = self.currentsavingbalance + amount 
        return self.currentsavingbalance

    def SavingWithdraw(self,amount):
        self.currentsavingbalance = self.currentsavingbalance - amount
        return self.currentsavingbalance

    def ChecquingDeposit(self,amount):
        self.currentchecquingbalance = self.currentchecquingbalance + amount
        return self.currentchecquingbalance

    def ChecquingWithdraw(self, amount):
        self.currentchecquingbalance = self.currentchecquingbalance - amount
        return self.currentchecquingbalance

# define savingAccount class
class SavingAccount(Account):
    
    def __init__(self,accountNumber, accountHolderName, rateOfinterest, currentchecquingbalance, currentsavingbalance):
        super().__init__(accountNumber, accountHolderName, rateOfinterest, currentchecquingbalance, currentsavingbalance)
        self.smin = 5000

        
    def Withdraw(self, amount):
        i = super().SavingWithdraw(amount)
        if i < self.smin:
            print("Yon can't withdraw too much money.")
            # display the original balance
            t = i + amount
            print("The balance is "+ str(t))
        else:
            print("Your current balance is: "+ str(i))
            
       
class ChequingAccount(Account):
    def __init__(self,accountNumber, accountHolderName, rateOfinterest, currentchecquingbalance, currentsavingbalance):
        super().__init__(accountNumber, accountHolderName, rateOfinterest, currentchecquingbalance, currentsavingbalance)
        self.overdraft = 5000

    def Withdraw(self,amount):
        i = super().ChecquingWithdraw(amount)
        if i > self.overdraft:
            print("You can't withdraw too much money.")
            t = i + amount
            print("The balance is "+ str(t))
        else:
            print("Yon current balance is: "+ str(i))



class Bank:
    
    user1 = [1111, "Leo", 5.3, 3000,8000]
    user2 = [2222,"Helen", 5.3, 3000,8000]
    user3 = [3333, "John", 5.3, 3000,8000]
    user4 = [4444, "Lily", 5.3, 3000,8000]
    user5 = [5555, "Howard", 5.3, 3000,8000]
    numbersearch =[user1[0],user2[0],user3[0],user4[0],user5[0]]
    namesearch = [user1[1],user2[1],user3[1],user4[1],user5[1]]
    numbersearch1 = [user1,user2,user3,user4,user5]

    def OpenAccount(self):
        
        
        print(Bank.user1,"\n",Bank.user2,"\n",Bank.user3,"\n",Bank.user4,"\n",Bank.user5)
        
        

    def SearchAccount(self):
        print("Please Select Following Options: ")
        choice = int(input("1.Enter Account \n2.Exit  "))
        if choice == 1:
            ii = int(input("Please input your Account Number: "))
            p = -1
            for i in Bank.numbersearch:
                if ii == i:
                        p = p+1
                        return Bank.numbersearch1[p]
                        
        else:
            print("Thank you for using our service.") 
                

class Program:
    def showMianMenu(self):
        t = Bank()
        print("Welcome To CIBC!")
        print("Account Information is As following: ")
        t.OpenAccount()
        user = t.SearchAccount()
        # initial Account Class
        global bankuser,bankusers,bankuserc
        bankuser = Account(user[0],user[1],user[2],user[3],user[4])
        bankusers = SavingAccount(user[0],user[1],user[2],user[3],user[4])
        bankuserc = ChequingAccount(user[0],user[1],user[2],user[3],user[4])

    def showAccountMenu(self):
        print("Please Select following Choice: ")
        choice = int(input("1.Checquing Account\n2.Saving Account\n3.Exit  "))
        if choice == 1:
            print("Please Select following Choice: ")
            checquingchoice = int(input("1.Check Balance\n2.Deposit\n3.Withdraw\n4.Exit Account "))
            if checquingchoice == 1:
                print("You current checquing balance is: "+str(bankuser.getCurrentChecquingBalance()))
                t = Program()
                t.showAccountMenu()
            elif checquingchoice == 2:
                depositamount = int(input("Please enter deposit amount: "))
                bankuserc.ChecquingDeposit(depositamount)
                print(bankuser.getCurrentChecquingBalance())
                t = Program()
                t.showAccountMenu()
            elif checquingchoice == 3:
                # call ChecquingAccount Method
                withdrawamount = int(input("Please enter withdraw amount: "))
                bankuserc.Withdraw(withdrawamount)
                print(bankuserc.getCurrentChecquingBalance())
                t = Program()
                t.showAccountMenu()
            else:
                t = Program()
                t.showMianMenu()
        elif choice == 2:
            print("Please Select following Choice: ")
            savingchoice = int(input("1.Check Balance\n2.Deposit\n3.Withdraw\n4.Exit Account "))
            if savingchoice == 1:
                print(bankuser.getCurrentSavingBalance())
                t = Program()
                t.showAccountMenu()
            elif savingchoice == 2:
                depositamount = int(input("Please enter deposit amount: "))
                bankuser.SavingDeposit(depositamount)
                print(bankuser.getCurrentSavingBalance())
                t = Program()
                t.showAccountMenu()
            elif savingchoice == 3:
                withdrawamount = int(input("Please enter withdraw amount: "))
                bankusers.Withdraw(withdrawamount)
                print(bankuser.getCurrentSavingBalance())
                t = Program()
                t.showAccountMenu()
            else:
                t = Program()
                t.showMianMenu()
        else:
            t = Program()
            t.showMianMenu()


