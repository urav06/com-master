import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import traceback
from Data.ItemList import *
from Data.Licence import *


class MainApplication:

    def __init__(self, parent, *args, **kwargs):
        self.frame = tk.Frame(master=parent, *args, **kwargs)  # Pack Style
        self.frame.pack(fill="both")

        self.main_notebook = ttk.Notebook(master=self.frame, width=860, height=720)
        self.main_notebook.pack(fill="both")


class AddLicenceTab:
    TAB_NAME = "New Licence"

    def __init__(self, parent, licence_list, save_function, *args, **kwargs):

        self.frame = tk.Frame(parent, *args, **kwargs)  # Grid Style
        tk.Tk.report_callback_exception = self.show_error
        parent.add(self.frame, text=self.TAB_NAME)
        self.input_frame = tk.Frame(master=self.frame)
        self.input_frame.place(relx=0.5, rely=0, anchor="n")

        # Data
        self.licence_list = licence_list
        self.item_list = ItemList()
        self.item_list_str = tk.StringVar()
        self.save_function = save_function

        # Entries and Buttons
        self.lic_num_entry = None
        self.issue_date_entry = None
        self.validity_entry = None
        self.exporter_entry = None
        self.agent_entry = None
        self.rupees_entry = None
        self.dollars_entry = None
        self.item_name_entry = None
        self.item_amount_entry = None
        self.add_item_button = None
        self.add_licence_button = None

        # Draw
        self.draw_labels()
        self.draw_entries()

    def draw_labels(self):
        tk.Label(master=self.input_frame, text="Licence Number").grid(row=0, column=0)
        tk.Label(master=self.input_frame, text="Issue Date(DD/MM/YYYY)").grid(row=1, column=0)
        tk.Label(master=self.input_frame, text="Validity(months)").grid(row=2, column=0)
        tk.Label(master=self.input_frame, text="Exporter name").grid(row=3, column=0)
        tk.Label(master=self.input_frame, text="Agent name").grid(row=4, column=0)
        tk.Label(master=self.input_frame, text="Value in rupees").grid(row=5, column=0)
        tk.Label(master=self.input_frame, text="Value in dollars").grid(row=6, column=0)
        ttk.Separator(master=self.input_frame).grid(row=7, columnspan=2, sticky="ew")
        tk.Label(master=self.input_frame, text="Item name").grid(row=8, column=0)
        tk.Label(master=self.input_frame, text="Amount in KG").grid(row=9, column=0)
        # row 10 has add item button
        ttk.Separator(master=self.input_frame).grid(row=11, columnspan=2, sticky="ew")
        tk.Label(master=self.input_frame, text="Items:").grid(row=12, columnspan=2)
        tk.Label(master=self.input_frame, textvariable=self.item_list_str).grid(row=13, columnspan=2)
        ttk.Separator(master=self.input_frame).grid(row=14, columnspan=2, sticky="ew")

    def draw_entries(self):

        self.lic_num_entry = tk.Entry(master=self.input_frame)
        self.lic_num_entry.grid(row=0, column=1)

        self.issue_date_entry = tk.Entry(master=self.input_frame)
        self.issue_date_entry.grid(row=1, column=1)

        self.validity_entry = tk.Entry(master=self.input_frame)
        self.validity_entry.insert(0, string="12")
        self.validity_entry.grid(row=2, column=1)

        self.exporter_entry = tk.Entry(master=self.input_frame)
        self.exporter_entry.grid(row=3, column=1)

        self.agent_entry = tk.Entry(master=self.input_frame)
        self.agent_entry.grid(row=4, column=1)

        self.rupees_entry = tk.Entry(master=self.input_frame)
        self.rupees_entry.grid(row=5, column=1)

        self.dollars_entry = tk.Entry(master=self.input_frame)
        self.dollars_entry.grid(row=6, column=1)
        # row 7 has separator
        self.item_name_entry = tk.Entry(master=self.input_frame)
        self.item_name_entry.grid(row=8, column=1)

        self.item_amount_entry = tk.Entry(master=self.input_frame)
        self.item_amount_entry.grid(row=9, column=1)

        self.add_item_button = tk.Button(master=self.input_frame, text="Add item", command=self.add_item)
        self.add_item_button.grid(row=10, columnspan=2)
        # row 11 has separator
        # row 12, 13 have items
        # row 14 has separator
        self.add_licence_button = tk.Button(master=self.input_frame, text="Add Licence", command=self.add_licence)
        self.add_licence_button.grid(row=15, columnspan=2)

    def add_item(self):
        item_name = self.item_name_entry.get()
        item_amount = self.item_amount_entry.get()

        try:
            item_name = item_name.lower()
            item_amount = int(item_amount)
            self.item_list.add_item(item_name, item_amount)
            self.item_list_str.set(str(self.item_list))

        except ValueError:
            raise Exception("Amount in KG should be a number only")

        self.item_name_entry.delete(0, 'end')
        self.item_amount_entry.delete(0, 'end')

    def add_licence(self):
        license_number = int(self.lic_num_entry.get())
        issue_date = Date(self.issue_date_entry.get())
        validity = int(self.validity_entry.get())
        exporter_name = self.exporter_entry.get()
        agent_name = self.agent_entry.get()
        rupees = int(self.rupees_entry.get())
        dollars = int(self.dollars_entry.get())
        item_list = self.item_list

        new_licence = Licence(license_number, issue_date, validity, exporter_name, agent_name,
                              rupees, dollars, item_list)

        self.lic_num_entry.delete(0, 'end')
        self.issue_date_entry.delete(0, 'end')
        self.validity_entry.delete(0, 'end')
        self.exporter_entry.delete(0, 'end')
        self.agent_entry.delete(0, 'end')
        self.rupees_entry.delete(0, 'end')
        self.dollars_entry.delete(0, 'end')
        self.item_list = ItemList()
        self.item_list_str.set("")

        self.licence_list.append(new_licence)
        self.save_function(self.licence_list)

    def show_error(self, *args):
        err = traceback.format_exception(*args)
        messagebox.showerror('Exception', err)


class ViewAllTab:
    TAB_NAME = "View all Licence"
    HEADINGS = ["Licence no.", "Issue Date", "Expiry Date", "Exporter", "Agent", "INR", "USD", "Items"]
    COLUMNS = ["#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8"]
    WIDTHS = [70, 70, 70, 100, 90, 50, 50, 650]

    def __init__(self, parent, licence_list, *args, **kwargs):
        self.notebook = parent

        self.frame = tk.Frame(master=parent, *args, **kwargs)
        parent.add(self.frame, text=self.TAB_NAME)

        # Data
        self.licence_list = licence_list

        # Search
        self.search_frame = tk.Frame(master=self.frame)     # Grid Style
        self.search_frame.pack()

        tk.Label(master=self.search_frame, text="Licence Number:").grid(row=0, column=3)
        self.open_licence_entry = tk.Entry(master=self.search_frame)
        self.open_licence_entry.grid(row=0, column=4)
        tk.Button(master=self.search_frame, text="Open", command=self.open_licence).grid(row=0, column=5)

        ttk.Separator(master=self.search_frame).grid(row=1, columnspan=8, sticky="ew")

        tk.Label(master=self.search_frame, text="Licence no:").grid(row=2, column=0)
        self.licence_no_Search = tk.Entry(master=self.search_frame)
        self.licence_no_Search.grid(row=2, column=1)

        ttk.Separator(master=self.search_frame, orient=tk.VERTICAL).grid(row=2, column=2, padx=5, sticky="ns")

        tk.Label(master=self.search_frame, text="Item:").grid(row=2, column=3)
        self.item_search = tk.Entry(master=self.search_frame)
        self.item_search.grid(row=2, column=4)

        ttk.Separator(master=self.search_frame, orient=tk.VERTICAL).grid(row=2, column=5, padx=5, sticky="ns")

        tk.Label(master=self.search_frame, text="Expiry Month:").grid(row=2, column=6)
        self.expiry_month_Search = tk.Entry(master=self.search_frame)
        self.expiry_month_Search.grid(row=2, column=7)

        self.search_button = tk.Button(master=self.search_frame, text="search/refresh", command=self.search)
        self.search_button.grid(row=3, columnspan=8)

        # Licence tree
        self.licence_tree_frame = tk.Frame(master=self.frame)
        self.licence_tree = ttk.Treeview(master=self.frame, show="headings", columns=self.COLUMNS)
        self.licence_list_to_print = self.licence_list
        self.draw_licence_tree()
        self.licence_tree.pack()
        self.licence_tree_frame.pack()

    def open_licence(self):
        licence_number = int(self.open_licence_entry.get())
        licence_to_open = None

        for licence in self.licence_list:
            if licence.lic_number == licence_number:
                licence_to_open = licence
                break
        if licence_to_open is not None:
            new_tab = LicenceTab(licence_to_open)
            self.notebook.add(new_tab.frame, text=new_tab.TAB_NAME)

    def search(self):
        licence_num_query = self.licence_no_Search.get()
        item_query = self.item_search.get()
        expiry_month_query = self.expiry_month_Search.get()

        self.licence_list_to_print = []

        for licence in self.licence_list:
            if licence_num_query == "" or licence_num_query in str(licence.lic_number):
                if item_query == "" or licence.item_present(item_query):
                    if expiry_month_query == "" or licence.expires_in_month(expiry_month_query):
                        self.licence_list_to_print.append(licence)

        self.draw_licence_tree()

    def draw_licence_tree(self):
        for i in self.licence_tree.get_children():
            self.licence_tree.delete(i)
        # Headings
        for i in range(len(self.COLUMNS)):
            self.licence_tree.heading(self.COLUMNS[i], text=self.HEADINGS[i], anchor=tk.CENTER)
            self.licence_tree.column(self.COLUMNS[i], minwidth=40, width=self.WIDTHS[i])

        # Data
        for licence in self.licence_list_to_print:
            tup = licence.to_str_tuple()
            self.licence_tree.insert("", tk.END, values=(tup[0], tup[1], tup[2], tup[3], tup[4], tup[5], tup[6], tup[7]))
        print(self.licence_list_to_print)


class LicenceTab:

    TAB_NAME = None

    def __init__(self, licence, *args, **kwargs):
        self.frame = tk.Frame(*args, **kwargs)
        self.licence = licence
        self.TAB_NAME = self.licence.lic_number

        self.header_frame = tk.Frame(master=self.frame, borderwidth=2, relief="raised")
        header = "Lic: " + str(self.licence.lic_number)
        tk.Label(master=self.header_frame, text=header, borderwidth=2, relief="ridge",
                 font="arial 14 bold").grid(row=0, columnspan=2)

        exporter_detail = "Exporter: "+self.licence.exporter_name
        tk.Label(master=self.header_frame, text=exporter_detail).grid(row=1, column=0)

        agent_detail = "Agent: "+self.licence.exporter_name
        tk.Label(master=self.header_frame, text=agent_detail).grid(row=2, column=0)

        issue_detail = "Issue Date: "+str(self.licence.issue_date)
        tk.Label(master=self.header_frame, text=issue_detail).grid(row=1, column=1)

        expiry_detail = "Expiry Date: "+str(self.licence.expiry_date)
        tk.Label(master=self.header_frame, text=expiry_detail).grid(row=2, column=1)

        self.header_frame.pack(fill="both")
