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

def queryNaive(x0, y0, x1, y1):
    count = 0

    x = naive[0]
    y = naive[1]
    for i in range(0,len(x)):
        if x0 <= x[i] <= x1 and y0 <= y[i] <= y1:
            count +=1
    return count

def queryOneDim(x0, y0, x1, y1):
    count = 0

    #create a list of bins according to n
    bins = onedim
    
    dim = 1/float(len(bins))
    
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

def queryTwoDim(x0, y0, x1, y1):
    count = 0

    #create a list of bins according to n
    bins = twodim
    
    dim = 1/float(len(bins))
    
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