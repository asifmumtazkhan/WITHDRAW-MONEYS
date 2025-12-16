class Bank: 
    def __init__(self): 
        self.bal=0
        self.pin="" 
        self.name=""
        self.Menu()
    def Menu(self):
        option=input('''
        1.Press 1 for seting Balance 
        2.Press 2 for setting Pin 
        3. Press 3 for setting Name
        4.Press 4 for withdrwal''')
        if option=="1":
            self.set_balance()
        elif option=="2":
            self.set_pin()
        elif option=="3":
            self.set_name()
        elif option=="4":
            self.withdrwal()
    def set_balance(self): 
        new_bal=int(input("Enter Your Balance")) 
        self.bal=new_bal
        self.Menu()
    def set_pin(self): 
        new_pin=input("Enter Pin") 
        self.pin=new_pin
        self.Menu()
    def set_name(self): 
        name=input("Enter Your Name")
        self.name=name 
        self.Menu()
    def withdrwal(self): 
        pin=input("Enter your  Pin")
        if self.pin==pin: 
            amount=int(input("Enter Amount"))
            if self.bal>amount:
                self.bal=self.bal- amount 
                print("Transaction Sucess")
                print(f"remaining amount {self.bal}")
        else:
            print("Wrong Pin Try Again")
            pin=input("Enter your  Pin") 
            if self.pin==pin:
                self.bal=self.bal- amount 
                print("Transaction Sucess")
                print(f"remaining amount {self.bal}")
            else: 
                exit()
        self.Menu()
c1=Bank()