import pickle
import os
from Licence import *


def save_data(licence_list):
    """
    Saves the list of licences in database

    :param licence_list: List of licences to be saved
    :return: None
    """
    file_name = "database.txt"

    with open(file_name, "wb") as save_file:
        pickle.dump(licence_list, save_file)


def load_list():
    """
    Loads the list of licences from the database

    :return: The list of licences saved
    """
    file_name = "database.txt"

    with open(file_name, "rb") as save_file:
        return pickle.load(save_file)


def read_new_licence():
    # READ: Licence number
    lic_number = input("Licence number:")

    # READ: Issue date
    success = False
    issue_date = None
    while not success:
        issue_date = input("Issue date (DD/MM/YYYY):")
        try:
            issue_date = issue_date.split(sep="/")
            day = int(issue_date[0])
            month = int(issue_date[1])
            year = int(issue_date[2])
            issue_date = Date(day, month, year)
            success = True
        except ValueError:
            print("Invalid date format")
        except IndexError:
            print("Invalid date format")
        except Exception as e:
            print(e)

    # READ: validity (months)
    success = False
    validity = None
    while not success:
        try:
            validity = int(input("Validity in months:"))
            success = True
        except ValueError:
            print("Enter numbers only")

    # READ: exporter
    exporter = input("Exporter name:")

    # READ: agent
    agent = input("Agent name:")

    # READ: rupees
    success = False
    rupees = None
    while not success:
        try:
            rupees = int(input("Value in rupees:"))
            success = True
        except ValueError:
            print("Enter numbers only.")

    # READ: dollars
    success = False
    dollars = None
    while not success:
        try:
            dollars = int(input("Value in dollars:"))
            success = True
        except ValueError:
            print("Enter numbers only.")

    # READ: number of items
    item_list = ItemList()
    success = False
    number_of_items = None
    while not success:
        try:
            number_of_items = int(input("Number of items:"))
            success = True
        except ValueError:
            print("Enter numbers only")

    # READ: items
    for _ in range(number_of_items):
        success = False
        while not success:
            try:
                item = input("item:")
                amount = int(input("amount in KG:"))
                item_list.add_item(item, amount)
                success = True
            except ValueError:
                print("Enter numbers only for amount in KG")
            except Exception as e:
                print(e)

    return lic_number, issue_date, validity, exporter, agent, rupees, dollars, item_list


if __name__ == "__main__":
    running = True
    loaded_list = load_list()

    while running:
        cmd = input("Command:")

        if cmd == "newlic":
            lic = read_new_licence()    # Licence signature as tuple
            new_lic = Licence(lic[0], lic[1], lic[2], lic[3], lic[4], lic[5], lic[6], lic[7])
            loaded_list.append(new_lic)
            save_data(loaded_list)

        if cmd == "display":
            print("{:^10} | {:^10} | {:^10} | {:^6}".format("LicenceNum", "IssueDate", "ExpiryDate", "dollars"))
            for lic in loaded_list:
                print("{:^10} | {:^10} | {:^10} | {:^6}$".format(lic.lic_number, str(lic.issue_date),
                                                                 str(lic.expiry_date), lic.balance_usd))

        elif cmd == "exit":
            running = False

        else:
            print("Invalid Command")
