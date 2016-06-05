# This script give access to Databases from a Server

class DatabaseConnect:
    
    ServerName = ""
    DatabaseName=""
    Port=0
    
    # Constructor of class
    def __init__(self, Server, Database, P):
    
        self.ServerName=Server
        self.DatabaseName=Database
        self.Port = P
        
        pass
        
    # This method connect to the Database        
    def ConnectDatabase(self):     
        return self.DatabaseName
        
    # This method close connection to the Database        
        
    def CloseConnection(self, ServerName, Database, Port):
        return Value                            
        
            