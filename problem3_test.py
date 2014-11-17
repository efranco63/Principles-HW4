xt = [0.825785921054066, 0.8939410143401887, 0.6725673404644138, 0.7167728362288949, 0.17702477990067467, 0.6096760658384218, 0.8880776528343874, 0.8093212501429666, 0.8599741856563748, 0.8211538253127405, 0.7571662725282077, 0.8307601639423229, 0.6040880807766437, 0.46029989119301973, 0.5780874629748957, 0.28363091445856026, 0.671821581980944, 0.7994520235772518, 0.5724668977009355, 0.5240647679340361]
yt = [0.5240177199803635, 0.8579819500172002, 0.31702318448141165, 0.9435248585458417, 0.9982854563857015, 0.8668981655915788, 0.4198491211854617, 0.020032284179866355, 0.4235350866567178, 0.4712129907690531, 0.5191916624669954, 0.5905548331215233, 0.1184429843925402, 0.5522589967219866, 0.3000671123456804, 0.5305906070323767, 0.2939155192658993, 0.6998871368851862, 0.7955579001417771, 0.9183999554846236]
points = []
for i in range(0,len(xt)):
    points.append((xt[i],yt[i]))

# Functions for students to implement.

naive = []
def buildNaive(points,n):
    del naive[:] #erasing previous data
    
    #create x and y vectors
    x = []
    y = []
    for i in points:
        x.append(i[0])
        y.append(i[1])
    
    #naive will consist of two lists: x and y
    naive.append(x)
    naive.append(y)
    return naive

onedim = []
def buildOneDim(points,n):
    del onedim[:] #erasing previous data
        
    #create n lists in onedim, each list containing (x,y) tuples in their respective partition
    dim = 1/float(n)
    for i in range(0,n):
        onedim.append([])
    for pair in points:
        onedim[int(pair[0]//dim)].append(pair)
    return onedim

twodim = []
def buildTwoDim(points,n):
    del twodim[:] #erasing previous data
    
    #create n lists in twodim, each list containing n lists which each contain (x,y) tuples according to the partitions
    for i in range(0,n):
        twodim.append([])
    for i in twodim:
        for j in range(0,n):
            i.append([])
        
    dim = 1.0/float(n)

    for pair in points:
        twodim[int(pair[0]//dim)][int(pair[1]//dim)].append(pair)
    
    return twodim

#print buildTwoDim(points,5)

def queryNaive(x0, y0, x1, y1):
    count = 0

    x = buildNaive(points,0)[0]
    y = buildNaive(points,0)[1]
    for i in range(0,len(x)):
        if x0 <= x[i] <= x1 and y0 <= y[i] <= y1:
            count +=1
    return count

#print queryNaive(0.7,0,1,1)

def queryOneDim(x0, y0, x1, y1):
    count = 0
    n = 5
    
    #create a list of bins according to n
    bins = buildOneDim(points,n)
    
    dim = 1/float(n)
    
    search_bins = []

    #determine in which bin x0 resides
    search_bins.append(int(x0//dim)) 
    
    #determine in which bin x1 resides
    search_bins.append(int(x1//dim))
           
    #search from x0's bin to x1's bin    
    for i in range(search_bins[0],search_bins[1]+1):
        for j in bins[i]:
            if x0 <= j[0] <= x1 and y0 <= j[1] <= y1:
                count += 1
    
    return count

print queryOneDim(0.7,0,1,1)

def queryTwoDim(x0, y0, x1, y1):
    count = 0
    n = 5

    #create a list of bins according to n
    bins = buildTwoDim(points,n)
    
    dim = 1/float(n)
    
    #search_bins will contain four elements, the bins in which x0,x1,y0,y1 reside, in that order
    search_bins = []
    
    #determine in which bin x0 resides
    search_bins.append(int(x0//dim))
            
    #determine in which bin x1 resides
    search_bins.append(int(x1//dim))
          
    #determine in which bin y0 resides
    search_bins.append(int(y0//dim))
        
    #determine in which bin y1 resides
    search_bins.append(int(y1//dim))

    #search from x0's bin to y1's bin
    for i in range(search_bins[0],search_bins[1]+1):
        for k in range(search_bins[2],search_bins[3]+1):
            for j in bins[i][k]:
                if x0 <= j[0] <= x1 and y0 <= j[1] <= y1:
                    count += 1
    
    return count 

#print queryTwoDim(0.7,0,1,1)