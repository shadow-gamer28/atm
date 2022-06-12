class Atm:
    def __init__(self, cardNumber, pin):
        self.cardNumber = cardNumber
        self.pin = pin
    
    def balanceinquiry(self):
        print("Your balance is: $10000")
    
    def cashwithdrawal(self, amount):
        new_amount = 10000 - amount
        print("You Withdrawed: " + str(amount) + " Your remaining balance is: " + str(new_amount))

def main():
    name = input("Hello what is your name?: ")
    print("Hello, " + name)
    cardNumber = input("Enter your Card Number: ")
    pin = input("Enter you Pin: ")
    new_user = Atm(cardNumber, pin)

    print("Choose your activity: ")
    print("1) Balance Inquiry")
    print("2) Cash withDrawel")
    activity = int(input("Enter your choise: "))

    if(activity == 1):
        new_user.balanceinquiry()
    elif(activity == 2):
        amount = int(input("Enter the amount: "))
        new_user.cashwithdrawal(amount)
    else:
        print("Enter a valid number!!")
    
if __name__ == "__main__":
    main()