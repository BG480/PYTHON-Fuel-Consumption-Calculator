import sqlite3


# Class that communicates with database.
class Database:

    # Constructor.
    def __init__(self):
        self.db_connection = None
        self.db_cursor = None

    # Connects to database (.sql file).
    def connect_to_database(self):
        self.db_connection = sqlite3.connect('database.db')
        self.db_cursor = self.db_connection.cursor()

    # Creates table if doesn't exist.
    def create_table_if_not_exists(self):
        self.db_connection.execute(
            "CREATE TABLE if not exists CONSUMPTION(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, DISTANCE REAL, LITRES REAL, COMBUSTION REAL);")
        self.db_connection.commit()

    # Inserts new record to table.
    def insert_record(self, distance, litres, consumption):
        self.db_connection.execute(
            "INSERT INTO CONSUMPTION(DISTANCE, LITRES, COMBUSTION) VALUES('" + str(distance) + "','" + str(
                litres) + "', '" + str(consumption) + "')")
        self.db_connection.commit()

    # Returns all records from table.
    def select_all_records(self):
        result = self.db_cursor.execute("SELECT * FROM CONSUMPTION")
        return result

    # Deletes record from table.
    def delete_record(self, index):
        self.db_connection.execute("DELETE FROM CONSUMPTION WHERE ID='" + str(index) + "';")
        self.db_connection.commit()

    # Calculates and returns the average fuel consumption from table.
    def calculate_average_fuel_consumption(self):
        self.db_cursor.execute("SELECT AVG(COMBUSTION) FROM CONSUMPTION")
        return self.db_cursor.fetchone()[0]

    # Returns number of records in table.
    def calculate_number_of_records(self):
        self.db_cursor.execute("SELECT COUNT(ID) FROM CONSUMPTION")
        return self.db_cursor.fetchone()[0]
