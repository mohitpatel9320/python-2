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
b1.openAccount("Mohit",101,1000)
print("*"*60)

while True:
    print("*"*60)
    print("1. Deposite ")
    print("2. Withdraw ")
    print("3. Check Balance ")
    print("4. Exit ")
    print("*"*60)
    choice=int(input("Enter Your Choice :"))
    print("*"*60)

    if choice==1:
        amount=int(input("Enter Amount : "))
        b1.deposit(amount)
        print("*"*60)

    elif choice==2:
        amount=int(input("Enter Withdrawal Amount : "))
        b1.withdraw(amount)
        print("*"*60)

    elif choice==3:
        b1.checkBalance()
        print("*"*60)

    elif choice==4:
        print("Thank You For Using Our Services")
        print("*"*60)
        break
    else:
        print("invalid choice.please try again.")
        print("*"*60)
