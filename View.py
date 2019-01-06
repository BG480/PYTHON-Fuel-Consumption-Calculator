from tkinter import *
from tkinter import messagebox

class AppView:


    '''
    The grid, pack, and place methods of every Tkinter widget operate in-place and always return None.
    This means that you cannot call them on the same line as you create a widget. Instead, they should be
    called on the line below:
    '''

    def __init__(self, root):

        # Set title of root window
        root.title("FUEL CONSUMPTION CALCULATOR")
        # Main window cannot be resized by user
        root.resizable(width=False, height=False)

        # Entry values
        self.litresEntryValue = DoubleVar(root, value=0.0)
        self.distanceEntryValue = DoubleVar(root, value=0.0)
        self.indexToDeleteEntryValue = IntVar(root, value=1)
        self.averageFuelConsumptionLabelValue = StringVar(root)

        # Scrollbar for listbox
        self.dataListboxScrollbar = Scrollbar(root)
        self.dataListboxScrollbar.grid(row=0, column=1, pady=10, rowspan=9, sticky=N + S + W)
        # Listbox that stores/presents data from databasae
        self.dataListbox = Listbox(root, width=70, yscrollcommand=self.dataListboxScrollbar.set)
        self.dataListbox.grid(row=0, column=0, rowspan=9, padx=(10, 0), pady=10,sticky=N + S + E + W)
        # scrollbar configuration - attach scrollbar to listbox
        self.dataListboxScrollbar.config(command=self.dataListbox.yview)

        # INSERT DATA SECTION
        self.insertLabel = Label(root, text="INSERT RECORD")
        self.insertLabel.grid(row=0, column=2, columnspan=2, padx=10, pady=5)
        self.litresLabel = Label(root, text="LITRES")
        self.litresLabel.grid(row=1, column=2)
        self.litresEntry = Entry(root, width=7, textvariable=self.litresEntryValue, justify=CENTER)
        self.litresEntry.grid(row=1, column=3, padx=10, pady=5)
        self.distanceLabel = Label(root, text="DISTANCE")
        self.distanceLabel.grid(row=2, column=2)
        self.distanceEntry = Entry(root, width=7, textvariable=self.distanceEntryValue, justify=CENTER)
        self.distanceEntry.grid(row=2, column=3, padx=10, pady=5)
        self.insertButton = Button(root, width=10, text="INSERT")
        self.insertButton.grid(row=3, column=2, columnspan=2, padx=10, pady=5)

        # DELETE DATA SECTION

        self.deleteLabel = Label(root, text="DELETE RECORD")
        self.deleteLabel.grid(row=4, column=2, columnspan=2, padx=10, pady=5)
        self.indexLabel = Label(root, text="INDEX")
        self.indexLabel.grid(row=5, column=2, padx=10, pady=5)
        self.indexToDeleteEntry = Entry(root, width=7, textvariable=self.indexToDeleteEntryValue, justify=CENTER)
        self.indexToDeleteEntry.grid(row=5, column=3, padx=10, pady=5)
        self.deleteButton = Button(root, width=10, text="DELETE")
        self.deleteButton.grid(row=6, column=2, columnspan=2, padx=10, pady=5)

        # STATS SECTION

        self.statisticsLabel = Label(root, text="STATISTICS")
        self.statisticsLabel.grid(row=7, column=2, columnspan=2, padx=10, pady=5)
        self.avgConsLabel = Label(root, text="AVG. CONS.")
        self.avgConsLabel.grid(row=8, column=2, padx=10, pady=5)
        self.averageFuelConsumptionLabel = Label(root, width=7, textvariable=self.averageFuelConsumptionLabelValue)
        self.averageFuelConsumptionLabel.grid(row=8, column=3, padx=10, pady=5)

    def showErrorMessageBox(self, title, message):
        messagebox.showerror(title, message)

