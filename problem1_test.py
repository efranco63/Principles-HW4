from datetime import datetime
from random import randint

#Create long list of values
#rand = []
#for i in range(0,10):
#    rand.append(str(randint(0,10)))

#for i in range(0,10000):
#    if i%2 > 0:
#        rand.append(str(0))
#    else:
#        rand.append(str(1))

#content = ''
#content = ','.join(rand)
#txtfile = open('test.txt','w')
#txtfile.write(content)
#txtfile.close



#f = open('test.txt')
#test = f.read()
#rand = []
#for i in test:
#    if i != ',':
#        rand.append(i)

# Functions for students to implement.
def solveOnlyLists(inputList):
    b = datetime.now()
    
    uniqueList = []
    #compute unique items in inputList
    for i in inputList:
        if not i in uniqueList:
            uniqueList.append(i)
            
    e = datetime.now()
    print str(e-b)
    
    return uniqueList

def solveDict(inputList):
    b = datetime.now()
    
    uniqueList = []
    in_dict = {}
    #compute unique items in inputList
    for i in inputList:
        if not i in in_dict:
            in_dict[i] = 1
    uniqueList = list(in_dict.keys())
    
    e = datetime.now()
    print str(e-b)
    
    return uniqueList

def solveSorted(sortedInputList):
    b = datetime.now()
    
    uniqueList = []
    in_dict = {}
    t = None
    #compute unique items in inputList
    for i in sortedInputList:
        if i != t:
            in_dict[i] = 1
            t = i
    uniqueList = list(in_dict.keys())
    
    e = datetime.now()
    print str(e-b)
    
    return uniqueList

rand = [0,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,9,0,1,9,0]
rand_s = sorted(rand)

print solveOnlyLists(rand)
print solveDict(rand)
print solveSorted(rand_s)