class Bank:
    def openAccount(self,name,acno,balance):
        self.name=name
        self.acno=acno
        self.balance=balance
        self.file=open(name,"w")
        self.file.write(f"Hello {name} Your Account Number {acno} is Opened With {balance} Rs .\n")
        self.file.close()
    def deposite(self,amount):
        self.balance=self.balance+amount
        self.file=open(self.name,"a")
        self.file.write(f"{self.name} is Deposite {amount} Rs .\n")
        self.file.close()
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
            self.file=open(self.name,"a")
            self.file.write(f"{self.name} is Withdrawl  {amount} Rs .\n")
            self.file.close()
        else:
            print(f"Sorry You Need Another {amount-self.balance} Rs .")
            self.file=open(self.name,"a")
            self.file.write(f"sorry {self.name} you neeed more {amount-self.balance} Rs for Withdrawl. \n")
            self.file.close()

    def checkBalance(self):
        print("Your Current Balance is : ",self.balance)
        self.file=open(self.name,"a")
        self.file.write(f"{self.name} your Current Balance is: {self.balance} Rs. \n")
        self.file.close()
b1=Bank()
#b1.openAccount("Mohit",101,1000)
print("*"*60)
while True:
    print("*"*60)
    print("1. Open Account ")
    print("2. Deposite ")
    print("3. Withdraw ")
    print("4. Check Balance ")
    print("5. Exit ")

    choice=int(input("Enter Your Choice : "))
    print("*"*60)

    
    if choice==1:
        name=input("Enter Your Name : ")
        acno=int(input("Enter Your Account Number : "))
        balance=int(input("Enter Balance : "))
        b1.openAccount(name,acno,balance)
        print("*"*60)
        
    elif choice==2:
        amount=int(input("Enter Amount You Want To Deposite : "))
        b1.deposite(amount)
        print("*"*60)

    elif choice==3:
        amount=int(input("Enter Withdrawl Amount : "))
        b1.withdraw(amount)
        print("*"*60)

    elif choice==4:
        b1.checkBalance()
        print("*"*60)
        
    elif choice==5:
        print("Thank You For Using Our Services .")
        print("*"*60)
        break
    
    else:
        print("Invalind Choice. Try Again.")
        break



