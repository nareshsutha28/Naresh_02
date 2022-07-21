class Bank:
    def account(self,sname,lname,balance):
        self.sname = sname
        self.lname = lname
        self.balance = balance
        print("Thank you, Mr/Mrs.",self.sname,self.lname, "your account balance is", self.balance,"Rs.")
    
    def deposit(self,ammount):
        self.balance = self.balance+ammount
        print("Ammount of", ammount,"Rs. are added in your account, Now Your balance is", self.balance,"Rs.")

    def withdraw(self, ammount):
        if self.balance>=ammount:
            self.balance = self.balance-ammount
            print("Ammount of", ammount,"Rs. are withdrawed from your account, Now Your balance is", self.balance,"Rs.")
        else:
            print("Insufficient balance, because your account balance is", self.balance,"Rs.")
    
    def status(self):
        print("Thank you for visiting our service, Mr/Mrs.",self.sname,self.lname, "your account balance is", self.balance,"Rs.")



s1 = Bank()
sname=input("Enter your First Name: ")
lname =input("Enter your Last Name: ")
balance= int(input("Enter your balance: "))
s1.account(sname,lname,balance)

while True:
    print("1. check balace \n2. Deposit ammount \n3. withdrawal ammount \n4. Exit")
    choice= int(input("Enter your Choice: "))
    if choice==1:
        s1.status()
    elif choice==2:
        ammount= int(input("Enter deposit ammount: "))
        s1.deposit(ammount)
    elif choice==3:
        ammount= int(input("Enter withdrawal ammount: "))
        s1.withdraw(ammount)                
    elif choice==4:
        print("Thank you for visiting our services.")
        break
    else :
        print("Enter valid choice.")
    


