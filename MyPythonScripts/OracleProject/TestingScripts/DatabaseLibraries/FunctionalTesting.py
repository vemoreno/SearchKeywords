# This script simulates functional tests to Database

class FunctionalTesting:

    # Constructor of class
    def __init__(self):
        pass
        
    # This method let know if the field allow nulls                
    def AllowNulls(self, DB, TableName, Field):
        return True

    # This method obtains the lenght allowed for the field         
    def CharacterLenght(self, DB, TableName, Field):
        return 20
        
    # This method let know the range of values for the field (Min and Max number)         
    def RangeOfValues(self, DB,  TableName, Field):
        return (0, 100)

    # This method let know if the field contains special characters        
    def ContainsSpecialCharacters(self, DB,  TableName, Field):
        return False  

    # This method let know if the field contains numbers        
    def ContainsNumbers(self, DB,  TableName, Field):
        return True 
    
    # This method let know if the field contains letters 
    def ContainsLetters(self, DB,  TableName, Field):
        return False                                                   