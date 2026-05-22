class Payment:
    def pay(self):
        print("Payment processing")

class CreditCard(Payment):
    def pay(self):
        print("Paid using Credit Card")

class UPI(Payment):
    def pay(self):
        print("Paid using UPI")

class Cash(Payment):
    def pay(self):
        print("Paid using Cash")

payments = [CreditCard(), UPI(), Cash()]

for p in payments:
    p.pay()