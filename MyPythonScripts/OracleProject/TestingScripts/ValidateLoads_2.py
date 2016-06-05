from DatabaseLibraries.LoadTesting import *
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
        
        Cont = 0
        LoadResults = []
        
        ObjectLoad = LoadTesting()
        
        LoadResults.append(ObjectLoad.SendLoadToTable(DB, "Sales", 30000))
        LoadResults.append(ObjectLoad.SendLoadToTable(DB, "Sales", 30000))
                    
        print "\nThe time for each load sent in the table was: \n "
        
        for L in LoadResults:
            print str(L) + " ms"
            
        LoadResults[:] = []   
        Cont = 0
            
        LoadResults.append(ObjectLoad.GetLoadFromTable(DB, "Sales"))
        LoadResults.append(ObjectLoad.GetLoadFromTable(DB, "Sales"))
            
        print "\nThe time for each load received in the table was: \n "
        
        for L in LoadResults:
            print str(L) + " ms"  
            
        LoadResults[:] = []   
        Cont = 0                 
            
        LoadResults.append(ObjectLoad.UpdateLoadFromTable(DB, "Sales"))
        LoadResults.append(ObjectLoad.UpdateLoadFromTable(DB, "Sales"))
		LoadResults.append(ObjectLoad.UpdateLoadFromTable(DB, "Sales"))
            
        print "\nThe time for each load update in the table was: \n "
        
        for L in LoadResults:
            print str(L) + " ms"                     
            
        EndTime = ObjectLoad.DeleteLoadFromTable(DB, "Sales")
        
        print "\nTime to delete all the load was: " + str(EndTime) + " ms"