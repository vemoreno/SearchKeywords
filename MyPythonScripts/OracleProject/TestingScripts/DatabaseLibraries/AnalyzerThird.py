import decimal

class Analyzer:

    PathFiles={}
    KeywordsList=()
    ExistKeyword=True
    
    def __init__(self, Kw, Paths):
    
        self.KeywordsList=Kw
        self.PathFiles=Paths
        
    def __GetMaxKeyword(self, Kw):
    
        Matches = 0
        Analysis = []
        KeywordAmount=[]
        
        Analysis.append(Kw)        
    
        for FileName, PathFound in self.PathFiles.items():        
            File = open(PathFound, "r")
            
            for L in File.readlines():
                Matches += L.count(Kw)

            KeywordAmount.append(Matches)
            Analysis.append(FileName)
            Analysis.append(Matches)
 
            Matches=0
            
        File.close()
        
        Analysis.append(True)
        #Analysis.append(max(KeywordAmount))
        Analysis.append(0)
        
        
                
        print Analysis     
        #return max(KeywordMatches)    
        
    def GetCoincidences(self):
        
        for Kw in self.KeywordsList:
            self.__GetMaxKeyword(Kw)