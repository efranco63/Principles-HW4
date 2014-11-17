def solveOnlyLists(inputList):
    uniqueList = []
    #compute unique items in inputList
    for i in inputList:
        if not i in uniqueList:
            uniqueList.append(i)    
    return uniqueList

def solveDict(inputList):    
    uniqueList = []
    in_dict = {}
    #compute unique items in inputList
    for i in inputList:
        if not i in in_dict:
            in_dict[i] = 1
    uniqueList = list(in_dict.keys())   
    return uniqueList

def solveSorted(sortedInputList):
    uniqueList = []
    t = None
    #compute unique items in sortedInputList
    for i in sortedInputList:
        if i != t:
            if not i in uniqueList:
                uniqueList.append(i)
            t = i
  
    return uniqueList