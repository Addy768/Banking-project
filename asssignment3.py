#my program Bank
li=[]
class Account:
    def  __init__(self, accountno, accountholdername, openingbalance, currentbalance) :
        self.accountno = accountno
        self.accountholdername = accountholdername 
        self.openingbalance=openingbalance
        self.rateofinterest = 4
        self.currentbalance = currentbalance
        self.deposit=0
        self.withdrawl=0
   ##  Gets the Account number
    def getAccountNo(self):
        self.accountno = input("Enter your Account no. :")
        if self.accountno=='' :
            print("account no cannot be blank")
        return self.accountno
    ##gets account holders name
    def getAccountHolderName(self):
        self.accountholdername = input("Enter your Account Name. :")
        if self.accountholdername=='' :
            print("account holder name cannot be blank")
        
        return self.accountholdername
##asks for opening balance
    def getOpeningBalance(self):
        self.openingbalance= float(input("Enter A/c Opening Balalance. :"))
        if self.openingbalance==0 :
            print("account opening balance cannot be 0")
        
        return self.openingbalance
#asks for roi details    
    def getRateOfInterest(self):
        self.rateofinterest = 10
        return self.rateofinterest
   #displays the current balance 
    def getCurrentBalance(self):
        self.currentbalance = self.openingbalance + self.deposit - self.withdrawl
        return self.currentbalance
#deposists the money
    def Deposit(self) :
        
        self.deposit = float(input("Enter amount to deposit:"))
        if self.deposit<=0 :
            print("account deposit cannot be 0")
        if self.deposit >800 :
            print("Amount is being overdrafted")
            

        return self.deposit
 #for withrawal inputs by user   
    def Withdrawl(self) :
        
        self.withdrawl = float(input("Enter amount to withdraw:"))
        if self.withdrawl<=0 :
            print("account withdrawal amount cannot be <0 ")

        if self.withdrawl >800 :
            print("Amount is being overdrafted")
             
        return self.withdrawl
    
##asks the user the anmount to be deposited
class SavingsAccount(Account):
    def __init__(self):
        minimumBalance=0
          
    def Deposit(self) :
        self.deposit = float(input("Enter amount to deposit:"))
        return self.deposit
#this withraws the amount from users acc
class ChecquingAccount (Account) :
    def __init__(self):
        overdraftAllowed=0

    def Withdrawal(self):
        self.withdrawl = float(input("Enter amount to withdrawa:"))
        return self.withdrawl
       
        
 #this diplays the data entered by the user         
    def dispData(self):
         
         print("Account information")
         print("===================")
         print("Account no      :",self.accountno)
         print("Account Name    :",self.accountholdername)
         print("Opening Balance :",self.openingbalance)
         print("Deposits        :",self.deposit)
         print("withdrawals     :",self.withdrawl)
         print("Account Balance :",self.currentbalance)
         print(li)
 #creating objects for all of them           
ob1 = Account("","",0,0)
ob4 = ChecquingAccount()
ob3 = SavingsAccount()

#MAIN MENU
while True :
    print("Bank Account Information")
    print("=====================")
    print("1.get Account no.")
    print("2.get Account Holder")
    print("3.get Opeing Balance")
    print("4.get Deposits")
    print("5.get Withdrawals")
    print("6.Check Current Balance")
    print("7.Display Account info.")
    print("8.Shutdown")
    print("")
    ans = int(input("Enter your Choice : 1-8 :"))
    if ans == 1 :
       ob1 = Account("","",0,0)
       while True :
        accno = ob1.getAccountNo()
        accname= ob1.getAccountHolderName()
        opbal = ob1.getOpeningBalance()
        currbal=opbal
        li.append(accno)
        li.append(accname)
        li.append(opbal)
        li.append(currbal)
        li.append(4)
        print(li)
        ans  = input("Thanks for using the state bank of India if you want to continue our service press y and to exit press n y/n :")
        if ans == 'n' :
            break

    #CHOICES BY THE USER   
    if ans == 2 :
       ob1.getAccountHolderName()
    if ans == 3 :
       ob1.getOpeningBalance()
    if ans == 4 :
       ob4.Deposit()
    if ans == 5 :
       ob3.Withdrawl()
    if ans == 6 :
       ob1.getCurrentBalance()
    if ans == 7 :
        print("your balance:", ob1.getCurrentBalance())
       #ob1.dispData()
    if ans == 8 :
        mclos = input("close application :y/n :")
        if mclos =='y' :
            break
#over  