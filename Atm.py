class Atm:
    def __init__ (self,Card,Pin,Name):
        self.Card = Card
        self.Pin = Pin
        self.Name = Name

    def balanceEnquiry(self):
        print("Your Bank balance is 10000000000")

    def cashWithdrawl(self,amount):
        Savings = 10000000000
        New_Amount = Savings - amount
        if New_Amount < Savings :
            print("You have withdrawn "+ str(amount) +" and your balance on account is:    " + str(New_Amount))


def main():
    print("Hello, Welcome to Mini Bank!!!")

    cardNum = int(input("Please enter the card number  (only 16 digits) : "))
    pinNum = int(input("Please enter the pin   (only 4 digits) : "))
    name = input("Please enter your  name  (only alphabetical characters) : ")

    newUser = Atm(cardNum, pinNum, name)

    print("Hello Our Dear customer "+ str(name) +",  What would you like to do?")
    print("1 = BalanceEnquiry and 2 = CashWithdrawl")
    activity = input("Enter the activity no : ")

    if activity == "1" :
        newUser.balanceEnquiry()

    elif activity == "2" :
        amount = int(input("What is the amount of Withdrawl ? : "))
        newUser.cashWithdrawl(amount)
    
    else :
        print("Oops!! Wrong number")

if __name__ == "__main__":
    main()