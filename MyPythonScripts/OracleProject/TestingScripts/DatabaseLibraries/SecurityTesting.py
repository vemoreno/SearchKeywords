# This script simulates security tests to Database

class SecurityTesting:
    
    # Constructor of class
    def __init__(self):
        pass
        
    # This method validate if the login is correct
    def ValidateLogin(self, DB, UserName, Password):
        return 29
        
    # This method validate if one user is active
    def ValidateUserState(self, DB, UserID):
        return True
    
    # This method validate if one user has permission to create objects
    # (Tables, Store Procedures, Triggers, Views)
    def ValidateCreateOfObjects(self, DB, UserID):
        return True        
        
    # This method validate if one user has permission to read objects
    # (Tables, Store Procedures, Triggers, Views)
    def ValidateReadObjects(self, DB, UserID):
        return True
        
    # This method validate if one user has permission to update objects
    # (Tables, Store Procedures, Triggers, Views)
    def ValidateUpdateObjects(self, DB, UserID):
        return True                
        
    # This method validate if one user has permission to delete objects
    # (Tables, Store Procedures, Triggers, Views)
    def ValidateDeleteObjects(self, DB, UserID):
        return True                