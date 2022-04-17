class ATM(object):
    def __init__(self, card_number, pin, balance):
        self.card_number = card_number
        self.pin = pin
        self.balance = balance

    def checkBalance(self, card_number, pin_number):
        if card_number == self.card_number and pin_number == self.pin:
            print("Your balance is $", self.balance)
        else:
            print("Input a valid card number or pin number")
        
    def withdrawal(self, card_number, pin_number, amount):
        if card_number == self.card_number and pin_number == self.pin and self.balance > amount:
            self.balance = self.balance - amount
            print("Withdraw successful, your balance is $", self.balance)
        else:
            print("Input a valid card number or pin number")
    
user = ATM("348965", 2940, 3069)

card_number = input("Enter your card number ")
pin_number = int(input("Enter you pin number "))

activity = int(input("Choose your activity 1. Balance Inquiry 2. Withdrawal "))

if activity == 1:
    user.checkBalance(card_number, pin_number)
elif activity == 2:
    amount = int(input("Enter amount to be withdrawn "))
    user.withdrawal(card_number, pin_number, amount)
else:
    print("Please enter a valid number")