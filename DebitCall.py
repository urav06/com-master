class DebitCall:

    def __init__(self, item, amount_kg, debit_inr, debit_usd):
        self.item = item
        self.amount_kg = amount_kg
        self.debit_inr = debit_inr
        self.debit_usd = debit_usd
        self.balance_before_debit_inr = None
        self.balance_before_debit_usd = None
        self.balance_after_debit_inr = None
        self.balance_after_debit_usd = None

    def process(self):
        self.balance_after_debit_inr = self.balance_before_debit_inr - self.debit_inr
        self.balance_after_debit_usd = self.balance_before_debit_usd - self.debit_usd
