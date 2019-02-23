from tkinter import *
from tkinter import messagebox


# Application's view (GUI).
class AppView:

    # Constructor that creates the layout.
    def __init__(self, root):
        # Sets title of root window.
        root.title("FUEL CONSUMPTION CALCULATOR")
        # Main window cannot be resized by user.
        root.resizable(width=False, height=False)

        # Scrollbar for listbox.
        self.data_listbox_scrollbar = Scrollbar(root)
        self.data_listbox_scrollbar.grid(row=0, column=1, pady=10, rowspan=9, sticky=N + S + W)
        # Listbox that stores/presents data from database.
        self.data_listbox = Listbox(root, width=70, yscrollcommand=self.data_listbox_scrollbar.set)
        self.data_listbox.grid(row=0, column=0, rowspan=9, padx=(10, 0), pady=10, sticky=N + S + E + W)
        # Scrollbar configuration - attaches scrollbar to listbox.
        self.data_listbox_scrollbar.config(command=self.data_listbox.yview)

        # "Insert record" section.
        self.insert_label = Label(root, text="INSERT RECORD")
        self.insert_label.grid(row=0, column=2, columnspan=2, padx=10, pady=5)
        self.litres_label = Label(root, text="LITRES")
        self.litres_label.grid(row=1, column=2)
        self.litres_entry = Entry(root, width=7, justify=CENTER)
        self.litres_entry.grid(row=1, column=3, padx=10, pady=5)
        self.distance_label = Label(root, text="DISTANCE")
        self.distance_label.grid(row=2, column=2)
        self.distance_entry = Entry(root, width=7, justify=CENTER)
        self.distance_entry.grid(row=2, column=3, padx=10, pady=5)
        self.insert_button = Button(root, width=10, text="INSERT")
        self.insert_button.grid(row=3, column=2, columnspan=2, padx=10, pady=5)

        # "Delete record" section.
        self.delete_label = Label(root, text="DELETE RECORD")
        self.delete_label.grid(row=4, column=2, columnspan=2, padx=10, pady=5)
        self.index_label = Label(root, text="INDEX")
        self.index_label.grid(row=5, column=2, padx=10, pady=5)
        self.index_to_delete_entry = Entry(root, width=7, justify=CENTER)
        self.index_to_delete_entry.grid(row=5, column=3, padx=10, pady=5)
        self.delete_button = Button(root, width=10, text="DELETE")
        self.delete_button.grid(row=6, column=2, columnspan=2, padx=10, pady=5)

        # "Stats" section.
        self.statistics_label = Label(root, text="STATISTICS")
        self.statistics_label.grid(row=7, column=2, columnspan=2, padx=10, pady=5)
        self.consumption_label = Label(root, text="AVG. CONS.")
        self.consumption_label.grid(row=8, column=2, padx=10, pady=5)
        self.average_fuel_consumption_label = Label(root, width=7)
        self.average_fuel_consumption_label.grid(row=8, column=3, padx=10, pady=5)

    # Shows error message box with info for user.
    def show_error_message_box(self, title, message):
        messagebox.showerror(title, message)
