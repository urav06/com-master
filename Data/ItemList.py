class ItemList:

    def __init__(self):
        self.item_dict = {}

    def __len__(self):
        return len(self.item_dict)

    def __str__(self):
        ret = ""
        for item, value in self.item_dict.items():
            ret += "{0}: {1}Kg\n".format(item, value)
        return ret

    def __repr__(self):
        return str(self.item_dict)

    def add_item(self, item, limit_kg):
        """
        Adds item to the list along with respective limit in KG. Raises exception if item already present.

        :param item: The Item e.g. paper, board, pvc, polyester
        :param limit_kg: The debit limit in KG
        :return: None
        """

        self.item_dict[item] = limit_kg

    def debit(self, item, amount_kg):
        """
        Debits an amount from the item in this licence

        :param item: The item from which amount is to be debited
        :param amount_kg: The amount to be debited in kg
        :return: None
        """
        if item not in self.item_dict:
            raise Exception("{} item not in licence".format(item))

        if amount_kg > self.item_dict[item]:
            raise Exception("Can not debit more than limit. Debit input = {}. Limit for {} = {}Kg"
                            .format(amount_kg, item, self.item_dict[item]))

        self.item_dict[item] -= amount_kg
