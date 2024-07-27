# Strategy interface
class PaymentStrategy:
    def pay(self, amount):
        pass

# Concrete Strategies
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal")

class CryptocurrencyPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using Cryptocurrency")

# Context
class PaymentProcessor:
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def process_payment(self, amount):
        self._strategy.pay(amount)

# Usage
payment_processor = PaymentProcessor(CreditCardPayment())
payment_processor.process_payment(100)

# Switch strategy
payment_processor.set_strategy(PayPalPayment())
payment_processor.process_payment(200)
