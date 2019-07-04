from Date import *
from ItemList import *
from DebitCall import *


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

    def debit(self, debit_call):
        debit_call.balance_before_debit_inr = self.balance_inr
        debit_call.balance_before_debit_usd = self.balance_usd
        debit_call.process()
        self.balance_inr = debit_call.balance_after_debit_inr
        self.balance_usd = debit_call.balance_after_debit_usd

        self.item_list.debit(debit_call.item, debit_call.amount_kg)
        self.debit_list.append(debit_call)
