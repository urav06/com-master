from Data.Date import *


class Licence:

    def __init__(self, lic_number, issue_date, validity_in_months, exporter_name, agent, rupees, dollars,
                 item_list):
        self.lic_number = lic_number
        self.issue_date = issue_date
        self.expiry_date = Date.add_months(issue_date, validity_in_months)
        self.exporter_name = exporter_name
        self.agent = agent
        self.balance_inr = rupees
        self.balance_usd = dollars
        self.item_list = item_list
        self.debit_list = []

    def __repr__(self):
        return str(self.lic_number)

    def debit(self, debit_call):
        debit_call.balance_before_debit_inr = self.balance_inr
        debit_call.balance_before_debit_usd = self.balance_usd
        debit_call.process()
        self.balance_inr = debit_call.balance_after_debit_inr
        self.balance_usd = debit_call.balance_after_debit_usd

        self.item_list.debit(debit_call.item, debit_call.amount_kg)
        self.debit_list.append(debit_call)

    def to_str_tuple(self):
        items = []
        for item, amount in self.item_list.item_dict.items():
            items.append((item, str(amount)))
        items = tuple(items)
        ret = (str(self.lic_number), str(self.issue_date), str(self.expiry_date), self.exporter_name, self.agent,
               str(self.balance_inr), str(self.balance_usd), items)
        return ret

    def item_present(self, item_query):
        for item in self.item_list.item_dict:
            if item_query in item:
                return True
        return False

    def expires_in_month(self, month):
        try:
            month = int(month)
        except ValueError:
            for word in Date.MONTH_TABLE:
                if month in word:
                    month = Date.MONTH_TABLE[word]

        if self.expiry_date.month == month:
            return True
        else:
            return False