from Gui import *
import pickle
from Data.Licence import *


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


if __name__ == "__main__":
    loaded_list = load_list()

    root = tk.Tk()
    root.state("zoomed")

    main_application = MainApplication(root)
    add_licence_tab = AddLicenceTab(main_application.main_notebook, loaded_list, save_data)
    view_all_tab = ViewAllTab(main_application.main_notebook, loaded_list)

    root.mainloop()
