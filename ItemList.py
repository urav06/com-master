class ItemList:

    def __init__(self):
        self.item_list = {}

    def add_item(self, item, limit_kg):
        """
        Adds item to the list along with respective limit in KG. Raises exception if item already present.

        :param item: The Item e.g. paper, board, pvc, polyester
        :param limit_kg: The debit limit in KG
        :return: None
        """

        if item in self.item_list:
            raise Exception("{} already added".format(item))

        self.item_list[item] = limit_kg

    def force_add_item(self, item, limit_kg):
        """
        Forcefully adds item to list. without checking if it already exists.

        :param item: The item to be added
        :param limit_kg: The debit limit in KG
        :return: None
        """
        self.item_list[item] = limit_kg

    def debit(self, item, amount_kg):
        """
        Debits an amount from the item in this licence

        :param item: The item from which amount is to be debited
        :param amount_kg: The amount to be debited in kg
        :return: None
        """
        if item not in self.item_list:
            raise Exception("{} item not in licence".format(item))

        if amount_kg > self.item_list[item]:
            raise Exception("Can not debit more than limit. Debit input = {}. Limit for {} = {}Kg"
                            .format(amount_kg, item, self.item_list[item]))

        self.item_list[item] -= amount_kg
