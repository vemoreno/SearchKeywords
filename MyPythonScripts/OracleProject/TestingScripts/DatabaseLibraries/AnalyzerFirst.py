import decimal

class Analyzer:

    PathFiles={}
    Keyword=""
    DiscountKeyword=0
    NotExistKeyword = False
    
    def __init__(self, Kw, Paths):
    
        self.Keyword=Kw
        self.PathFiles=Paths
  
    def GetCoincidences(self):
    
        DictionaryReport = {}
        CoincidencesList = []
        Matches = 0
        GotMatchesFirstFile = False
        TotalMatchesFirstFile = 0

        for FileName, PathFound in self.PathFiles.items():        
            File = open(PathFound, "r")
        
            for L in File.readlines():
                Matches += L.count(self.Keyword)
                
            if(GotMatchesFirstFile == False):                

                TotalMatchesFirstFile = Matches                
                CoincidencesList.append([FileName, Matches])
                GotMatchesFirstFile = True
                
                DictionaryReport[self.Keyword] = CoincidencesList
                
            else:
            
                Block1 = []
                Block2 = []
            
                CoincidencesList.append([FileName, Matches])
                V = self.__GetPercentage(TotalMatchesFirstFile, Matches)

                Block1.append(V)
                CoincidencesList.append(Block1)
                
                if(Matches==0 and TotalMatchesFirstFile==0):
                    self.NotExistKeyword = True
                
                Block2.append(self.NotExistKeyword)
                #CoincidencesList.append(Block2)                
                DictionaryReport[self.Keyword] = CoincidencesList
                
            Matches=0
    
        File.close()
        

        return DictionaryReport
            
    def __GetPercentage(self, MatchesFile1, MatchesFile2):

        if(MatchesFile1>=MatchesFile2):
            if(MatchesFile1>0):
                V = decimal.Decimal((MatchesFile2*100)/MatchesFile1)
            else:
                return 0
        else:       
            if(MatchesFile2>0):
                V = decimal.Decimal((MatchesFile1*100)/MatchesFile2)
            else:
                return 0
        
        return V
        
    def GetSimilarityPercentage(self, FinalReport, TotalKeywords):
    
        Cont = 0
        TotalPercentage = 0
                            
        for Dictionary in FinalReport:
            for Key in Dictionary.keys():
                for List in Dictionary[Key]:
                    if(Cont==2):
                        s = map(str, List)
                        TotalPercentage += int(s[0])
                        Cont=-1
                        
                    Cont+=1  
                    
        for I in FinalReport:
            print I                    

        Result = round(decimal.Decimal(TotalPercentage) / decimal.Decimal(TotalKeywords),2)                     
        print "\nPercentage of similiarty: " + str(Result) + " %"                    