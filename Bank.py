

class Program:
    def showMainMenu(self):
        # while loop to display the following options until the user to choose to exit the application
        print("Please select your account：")
        print("1. Open Account \n2. Select Account \n3. Exit")
        i = int(input("Please Enter: "))
        while (i != 3):
            print("1. Open Account \n2. Select Account \n3. Exit")
            i = int(input("Please Enter: "))
            if (i == 1):
                pass
            elif (i == 2):
                pass
        print("Exit")
        return
    
    # define showAccountMenu
    def showAccountMenu(self):
        print("Please select following options: ")
        print("1. Check Balance \n2. Deposit \n3. Withdraw \n4.Exit Account")
        i = int(input("Please enter: "))
        while (i != 4):
            if (i == 1):
                pass
            elif (i == 2):
                pass
            elif (i ==3):
                pass
        print("Exit Account")
        t = Program()
        t.showMainMenu()

# define class bank, it will record accounts information and method search account, open account
class Bank:
    # create 5 accounts with hard coded values
    def __init__(self):
        self.user1 = ["Kevin", 1111, "aaaa", 6000]
        self.user2 = ["James", 2222, "bbbb", 6000]
        self.user3 = ["Leo", 3333, "cccc", 6000]
        self.user4 = ["Linda", 4444, "dddd", 6000]
        self.user5 = ["Helen", 5555, "eeee", 6000]
        
    
    # Define the searchaccount method that accepts an account number as parameter
    def searchAccount(self, number):
        #
            if number == self.user1[1]:
                return self.user1
            elif number == self.user2[1]:
                return self.user2
            elif number == self.user3[1]:
                return self.user3
            elif number == self.user4[1]:
                return self.user4
            elif number == self.user5[1]:
                return self.user5
            else:
                return 

class Account:
    def SavingsAccount(self,a):
        
        





