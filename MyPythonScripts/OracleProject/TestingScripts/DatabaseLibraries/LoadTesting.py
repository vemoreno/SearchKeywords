# This script simulates load tests to Database

class LoadTesting:
    
    # Constructor of class
    def __init__(self):
        pass
        
    # This method send heavy load to tables
    def SendLoadToTable(self, DB, TableName, Records):
        return 5000        
        
    # This method get load sent from a table        
    def GetLoadFromTable(self, DB, TableName):
        return 10000           
        
    # This method delete load from a table
    def DeleteLoadFromTable(self, DB, TableName):
        return 7500        
        
    # This method update load from a table
    def UpdateLoadFromTable(self, DB, TableName):
        return 6400        