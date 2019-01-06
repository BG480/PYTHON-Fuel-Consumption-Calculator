import sqlite3


class Database:

    def __init__(self):
        self.dbConnection = 0
        self.dbCursor = 0

    # connects to database .sql file
    def ConnectToDatabase(self):
        self.dbConnection = sqlite3.connect('database.db')
        self.dbCursor = self.dbConnection.cursor()

    # creates table if doesn't exist
    def CreateTableIfNotExist(self):
        self.dbConnection.execute(
            "CREATE TABLE if not exists CONSUMPTION(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, DISTANCE REAL, LITRES REAL, COMBUSTION REAL);")
        self.dbConnection.commit()

    # inserts new record to database
    def InsertRecord(self, distance, litres, consumption):
        self.dbConnection.execute(
            "INSERT INTO CONSUMPTION(DISTANCE, LITRES, COMBUSTION) VALUES('" + str(distance) + "','" + str(
                litres) + "', '" + str(consumption) + "')")
        self.dbConnection.commit()

    # returns all records from database
    def SelectAllRecords(self):
        result = self.dbCursor.execute("SELECT * FROM CONSUMPTION")
        return result

    # deletes record  from database
    def DeleteRecord(self, index):
        self.dbConnection.execute("DELETE FROM CONSUMPTION WHERE ID='" + str(index) + "';")
        self.dbConnection.commit()

    # calculates and returns the average fuel consumption from database
    def CalculateAverageFuelConsumption(self):
        self.dbCursor.execute("SELECT AVG(COMBUSTION) FROM CONSUMPTION")
        return self.dbCursor.fetchone()[0]

    # calculates and returns number of record in databse
    def CalculateNumberOfRecords(self):
        self.dbCursor.execute("SELECT COUNT(ID) FROM CONSUMPTION")
        return self.dbCursor.fetchone()[0]
