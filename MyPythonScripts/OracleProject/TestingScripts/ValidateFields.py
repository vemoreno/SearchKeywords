from DatabaseLibraries.FunctionalTesting import *
from DatabaseLibraries.SecurityTesting import *
from DatabaseLibraries.DatabaseConnect import * 

ObjectDataBase = DatabaseConnect("localhost", "TestingDatabase",80)
DB = ObjectDataBase.ConnectDatabase()

ObjectSecurity = SecurityTesting()
UserID = ObjectSecurity.ValidateLogin(DB, "vmoreno","pass123")

if (UserID > 0 ):

    Result = False
    Result = ObjectSecurity.ValidateUserState(DB, Result)
    
    if(Result == True):
    
        ValidationsResult = []
        
        ObjectFunctional = FunctionalTesting()        
        if(ObjectFunctional.AllowNulls(DB, "Products", "UnitPrice")==True):
            ValidationsResult.append("Field UnitPrice Allow nulls")
        else:
            ValidationsResult.append("Field UnitPrice Not allow nulls")                        
        
        Lenght = ObjectFunctional.CharacterLenght(DB, "Products", "UnitPrice")
        ValidationsResult.append("Field UnitPrice max lenght " + str(Lenght))
                
        Range = ObjectFunctional.RangeOfValues(DB, "Products", "UnitPrice")
        ValidationsResult.append("Field UnitPrice range (Min, Max): ")
        ValidationsResult.append(Range)
        
        if (ObjectFunctional.ContainsSpecialCharacters(DB, "Products", "UnitPrice")==True):
            ValidationsResult.append("Field UnitPrice contains special characters")
        else:
            ValidationsResult.append("Field UnitPrice not contains special characters")
        
        if (ObjectFunctional.ContainsNumbers(DB, "Products", "UnitPrice")==True):
            ValidationsResult.append("Field UnitPrice contains numbers")

        else:            
            ValidationsResult.append("Field UnitPrice not contains numbers")
            
        if (ObjectFunctional.ContainsLetters(DB, "Products", "UnitPrice")==True):
            ValidationsResult.append("Field UnitPrice contains letters")

        else:            
            ValidationsResult.append("Field UnitPrice not contains letters") 
            
        print "\nIn the Database, the table products was validated: \n "
    
        for V in ValidationsResult:
            print V                                              
        