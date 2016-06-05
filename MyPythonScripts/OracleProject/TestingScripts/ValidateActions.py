# This script make load test to the database 

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
    
        PermissionList = []
    
        if(ObjectSecurity.ValidateCreateOfObjects(DB, UserID)==True):
            PermissionList.append("Create")
        
        if(ObjectSecurity.ValidateReadObjects(DB, UserID)==True):
            PermissionList.append("Read")           

        if(ObjectSecurity.ValidateUpdateObjects(DB, UserID)==True):
            PermissionList.append("Update")           

        if(ObjectSecurity.ValidateDeleteObjects(DB, UserID)==True):
            PermissionList.append("Delete")    
            
    print "\nIn the Database, the user vmoreno have permissions to: \n "
    
    for P in PermissionList:
            print P                                                                