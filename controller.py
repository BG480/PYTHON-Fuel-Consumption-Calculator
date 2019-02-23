import tkinter
import model
import view


# Application's controller.
class AppController:

    # Class constructor.
    def __init__(self):
        self.root = tkinter.Tk()  # main window of application
        self.app_view = view.AppView(self.root)  # creates app's view
        self.app_model = model.Database()  # creates app's model
        self.app_view.insert_button.config(command=self.add_record)  # bind method to button
        self.app_view.delete_button.config(command=self.delete_record)  # bind method to button

    # Starts the application.
    def start(self):
        try:
            self.app_model.connect_to_database()
            self.app_model.create_table_if_not_exists()
            self.update_view()
        except model.sqlite3.OperationalError as ex:
            self.app_view.show_error_message_box("DATABASE ERROR", "SQLite error: {0} ".format(ex))
        except ValueError:
            self.app_view.show_error_message_box("ERROR", "Invalid data !")
        self.root.mainloop()

    # Adds new record to database.
    def add_record(self):
        try:
            litres = float(self.app_view.litres_entry.get())
            distance = float(self.app_view.distance_entry.get())
            self.app_model.insert_record(distance, litres, (litres / (distance / 100)))
            self.update_view()
        except model.sqlite3.OperationalError as ex:
            self.app_view.show_error_message_box("ERROR", "SQLite error: {0} ".format(ex))
        except ValueError:
            self.app_view.show_error_message_box("ERROR", "Invalid data !")

    # Deletes chosen record (by index) from database.
    def delete_record(self):
        try:
            index = int(self.app_view.index_to_delete_entry.get())
            self.app_model.delete_record(index)
            self.update_view()
        except model.sqlite3.OperationalError as ex:
            self.app_view.show_error_message_box("DATABASE ERROR", "SQLite error: {0} ".format(ex))
        except ValueError:
            self.app_view.show_error_message_box("ERROR", "Invalid data !")

    # Updates listbox and consumption label shown in GUI.
    def update_view(self):
        try:
            self.app_view.data_listbox.delete(0, tkinter.END)  # deletes all records from listbox
            database_records = self.app_model.select_all_records()  # gets all records from database
            for row in database_records:  # loop that inserts records from database to listbox
                self.app_view.data_listbox.insert(row[0],
                                                  "ID: {:d} | DISTANCE: {:.2f} | LITRES: {:.2f} | FUEL CONSUMPTION: {:.2f}".format(
                                                      row[0], row[1], row[2], row[3]))
            avg_consumption = self.app_model.calculate_average_fuel_consumption()
            self.app_view.average_fuel_consumption_label[
                'text'] = "0.00" if avg_consumption is None else "{:.2f}".format(avg_consumption)  # ternary operator
        except model.sqlite3.OperationalError as ex:
            self.app_view.show_error_message_box("ERROR", "SQLite error: {0} ".format(ex))
