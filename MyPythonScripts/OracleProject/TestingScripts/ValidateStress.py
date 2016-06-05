from DatabaseLibraries.StressTesting import *
from DatabaseLibraries.SecurityTesting import *
from DatabaseLibraries.DatabaseConnect import * 

ObjectDataBase = DatabaseConnect("localhost", "TestingDatabase",80)
DB = ObjectDataBase.ConnectDatabase()

ObjectSecurity = SecurityTesting()
UserID = ObjectSecurity.ValidateLogin(DB, "vmoreno","pass123")

if (UserID > 0):

    Result = False
    Result = ObjectSecurity.ValidateUserState(DB, Result)
    
    if(Result == True):
    
        ConnectionList = []
        
        Cont = 0 
        ObjectStress = StressTesting()

        while (Cont<=2):        
            ConnectionList.append(ObjectStress.SimulateConnection(DB, UserID, 45, 1500))
            Cont+=1
            
        print "\nResult for all connections for the user vmoreno: \n"
        
        for C in ConnectionList:
            print str(C)    
            
        ObjectStress.CloseConnection(DB, UserID)        
        print "\nAll connections for the user vmoreno was closed"