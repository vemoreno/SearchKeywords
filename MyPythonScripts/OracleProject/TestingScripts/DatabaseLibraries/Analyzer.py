import decimal

class Analyzer:

    PathFiles={}
    Keyword=""
    ExistKeyword=True
    
    def __init__(self, Kw, Paths):
    
        self.Keyword=Kw
        self.PathFiles=Paths
  
    def GetCoincidences(self):
    
        CoincidencesList = []
        Matches = 0
        GotMatchesFirstFile = False
        TotalMatchesFirstFile = 0

        for FileName, PathFound in self.PathFiles.items():        
            File = open(PathFound, "r")
        
            for L in File.readlines():
                Matches += L.count(self.Keyword)
                
            if(GotMatchesFirstFile == False):                

                CoincidencesList.append(self.Keyword)
                
                TotalMatchesFirstFile = Matches                
                CoincidencesList.append(FileName)
                CoincidencesList.append(Matches)
                GotMatchesFirstFile = True
                
            else:
            
                CoincidencesList.append(FileName)
                CoincidencesList.append(Matches)
                
                V = self.__GetPercentage(TotalMatchesFirstFile, Matches)

                CoincidencesList.append(V)
                
                if(Matches==0 and TotalMatchesFirstFile==0):
                    self.ExistKeyword = False
                
                CoincidencesList.append(self.ExistKeyword)                
                
            Matches=0
    
        File.close()

        print CoincidencesList
        return CoincidencesList 
            
    def __GetPercentage(self, MatchesFile1, MatchesFile2):

        if(MatchesFile1>=MatchesFile2):
            if(MatchesFile1>0):
                V = round((decimal.Decimal(MatchesFile2)*100)/decimal.Decimal(MatchesFile1), 2)
            else:
                return 0
        else:       
            if(MatchesFile2>0):
                V = round((decimal.Decimal(MatchesFile1)*100)/decimal.Decimal(MatchesFile2), 2)
            else:
                return 0
        
        return V
        
    def GetSimilarityPercentage(self, FinalReport, TotalKeywords):

        Discount = 0
        TotalPercentage = 0
    
        for L in FinalReport:
            TotalPercentage+=L[5]
            
            if(L[6]==False):  
                Discount+=1
        
        if((TotalKeywords-Discount)>0):
            Result = round(decimal.Decimal(TotalPercentage) / decimal.Decimal(TotalKeywords - Discount),2)                     
            print "\nPercentage of similiarty: " + str(Result) + " %"
            
        else:
            print "\nPercentage of similiarty: 0%"
            
        