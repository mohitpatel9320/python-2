class Bank:
    def openAccount(self,cname,acno,balance):
        self.cname=cname
        self.acno=acno
        self.balance=balance
        print("Hello ",cname," your Account Number ",acno," Is opened With ",balance," Rs .")
    def deposit(self,amount):
        self.balance=self.balance+amount
    
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
        else:
            print("Sorry You Need Another ",amount-self.balance," Rs .")

    def checkBalance(self):
        print("Your current Balance is :",self.balance)

b1=Bank()
print("*"*60)
#b1.openAccount("Mohit",101,1000)
#print("*"*60)

while True:
    print("*"*60)
    print("1. Open Account")
    print("2. Deposite ")
    print("3. Withdraw ")
    print("4. Check Balance ")
    print("5. Exit ")
    print("*"*60)
    choice=int(input("Enter Your Choice :"))
    print("*"*60)
    if choice==1:
        name=input("Enter Your Name : ")
        acno=int(input("Enter Your Account Number : "))
        balance=int(input("Enter Balance : "))
        b1.openAccount(name,acno,balance)
        print("*"*60)
    elif choice==2:
        amount=int(input("Enter Amount You Want to Deposite : "))
        b1.deposit(amount)
        print("*"*60)

    elif choice==3:
        amount=int(input("Enter Withdrawal Amount : "))
        b1.withdraw(amount)
        print("*"*60)

    elif choice==4:
        b1.checkBalance()
        print("*"*60)

    elif choice==5:
        print("Thank You For Using Our Services")
        print("*"*60)
        break
    else:
        print("invalid choice.please try again.")
        print("*"*60)
        break
