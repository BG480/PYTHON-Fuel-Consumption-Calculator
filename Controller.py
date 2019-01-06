import tkinter as tk
from Model import *
from View import *


class AppController:
    #initialize method
    def __init__(self):
        self.root = tk.Tk() #main window of application
        self.view = AppView(self.root) #create apps view
        self.model = Database() #create apps model
        self.view.insertButton.config(command = self.addData)
        self.view.deleteButton.config(command = self.deleteData)


    #starts the application
    def start(self):
        try:
            self.model.ConnectToDatabase()
            self.model.CreateTableIfNotExist()
            self.updateViewData()
        except sqlite3.OperationalError as ex:
            self.view.showErrorMessageBox("ERROR", "SQLite error: {0} ".format(ex))
        except ValueError as ex:
            self.view.showErrorMessageBox("ERROR", "Something bad happened: .".format(ex))
        self.root.mainloop()

    #add new data to database
    def addData(self):
        try:
            litres = self.view.litresEntryValue.get()
            distance = self.view.distanceEntryValue.get()
            self.model.InsertRecord(distance, litres, (litres / (distance / 100)))
            self.updateViewData()
        except sqlite3.OperationalError as ex:
            self.view.showErrorMessageBox("ERROR", "SQLite error: {0} ".format(ex))
        except Exception as ex:
            self.view.showErrorMessageBox("ERROR", "Something bad happened: .".format(ex))

    #deletes chosen data (by index) from database
    def deleteData(self):
        try:
            index = self.view.indexToDeleteEntryValue.get()
            self.model.DeleteRecord(index)
            self.updateViewData()
        except sqlite3.OperationalError as ex:
            self.view.showErrorMessageBox("ERROR", "SQLite error: {0} ".format(ex))
        except:
            self.view.showErrorMessageBox("ERROR", "Something bad happened: .".format(sys.exc_info()[0]))

    #updates the database data shown for user in view
    def updateViewData(self):
        try:
            self.view.dataListbox.delete(0, END) #deletes all records from listbox
            databaseRecords = self.model.SelectAllRecords() #gets all records from database
            for row in databaseRecords: #loop that inserts records from database to listbox
                self.view.dataListbox.insert(row[0],
                                        "ID: {:d} | DISTANCE: {:.2f} | LITRES: {:.2f} | FUEL CONSUMPTION: {:.2f}".format(
                                            row[0], row[1], row[2], row[3]))
            numberOfRecords = self.model.CalculateNumberOfRecords()
            if numberOfRecords > 0:
                avgConsumption = self.model.CalculateAverageFuelConsumption()  # gets average fuel consumption from database
                self.view.averageFuelConsumptionLabelValue.set("{:.2f}".format(avgConsumption))  # updates label value that displays average consumption
            else:
                self.view.averageFuelConsumptionLabelValue.set("0.0")
        except sqlite3.OperationalError as ex:
            self.view.showErrorMessageBox("ERROR", "SQLite error: {0} ".format(ex))
        except:
            self.view.showErrorMessageBox("ERROR", "Something bad happened: .".format(sys.exc_info()[0]))

