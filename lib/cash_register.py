class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction_amount = 0

    def add_item(self, title, price, quantity=1):
        item_total = price * quantity
        self.total += item_total
        self.items.extend([title] * quantity)
        self.last_transaction_amount = item_total

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            return f"After the discount, the total comes to ${self.total:.2f}."
        else:
            return "There is no discount to apply."

    def void_last_transaction(self):
        if self.last_transaction_amount > 0:
            self.total -= self.last_transaction_amount
            self.items.pop()
            if not self.items:
                self.total = 0.0
        else:
            return "No items to void."

    def get_items(self):
        return self.items

    def get_total(self):
        return self.total
