from DatabaseLibraries.Analyzer import *

KeywordsList = (
                "ValidateLogin", 
                "ValidateUserState",
                "SimulateConnection",
                "CloseConnection",
                #"SendLoadToTable",
                #"GetLoadFromTable",
                #"DeleteLoadFromTable",
                #"UpdateLoadFromTable",
                )
                                                
PathFiles ={
            #"ValidateActions"  : "MyPythonScripts/OracleProject/TestingScripts/ValidateActions.py",
            #"ValidateFields"   : "MyPythonScripts/OracleProject/TestingScripts/ValidateFields.py",
            #"Script ValidateLoads"    : "MyPythonScripts/OracleProject/TestingScripts/ValidateLoads.py", 
            #"Script ValidateLoads2"  : "MyPythonScripts/OracleProject/TestingScripts/ValidateLoads_2.py",
            "ValidateStress"    :   "MyPythonScripts/OracleProject/TestingScripts/ValidateStress.py",
            "ValidateStress_2"  : "MyPythonScripts/OracleProject/TestingScripts/ValidateStress_2.py",
           }
           
FinalReport = []          

if(len(PathFiles)==2):

    for Kw in KeywordsList:
        
        ObjectAnalyzer = Analyzer(Kw, PathFiles)
        FinalReport.append(ObjectAnalyzer.GetCoincidences())

    ObjectAnalyzer.GetSimilarityPercentage(FinalReport, len(KeywordsList))
    
else:
     print "It's necesary to compare, only two path files"