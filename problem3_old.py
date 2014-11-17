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

    #create x and y vectors
    x = []
    y = []
    for i in points:
        x.append(i[0])
        y.append(i[1])
        
    #create n lists in onedim, each list containing (x,y) tuples in their respective partition
    for i in range(0,n):
        onedim.append([])
    dim = 1.0/float(n)
    for i in range(0,len(x)):
        if 0 <= x[i] <= dim:
            onedim[0].append((x[i],y[i]))
        for j in range(1,n):                
            if j * dim < x[i] <= (j+1) * dim:
                onedim[j].append((x[i],y[i]))
    return onedim

twodim = []
def buildTwoDim(points,n):
    del twodim[:] #erasing previous data

    #create x and y vectors
    x = []
    y = []
    for i in points:
        x.append(i[0])
        y.append(i[1])
    
    #create n lists in twodim, each list containing n lists which each contain (x,y) tuples according to the partitions
    for i in range(0,n):
        twodim.append([])
    for i in twodim:
        for j in range(0,n):
            i.append([])
        
    dim = 1.0/float(n)
    for i in range(0,len(x)):
        #check first column first row
        if 0 <= x[i] <= dim:
            if 0 <= y[i] <= dim:
                twodim[0][0].append((x[i],y[i]))
            #remaining in the first column, move up rows
            for k in range(1,n):
                if k * dim < y[i] <= (k+1) * dim:
                    twodim[0][k].append((x[i],y[i]))
        #move across columns left to right
        for j in range(1,n):                
            if j * dim < x[i] <= (j+1) * dim:
                if 0 <= y[i] <= dim:
                    twodim[j][0].append((x[i],y[i]))
                #remaining in the jth column, move up rows
                for q in range(1,n):
                    if q * dim < y[i] <= (q+1) * dim:
                        twodim[j][q].append((x[i],y[i]))
    
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
    
    #get a list of the dimension partition points
    dims = []
    for i in range(1,len(bins)+1):
        dims.append(i/float(len(bins)))
    
    #search_bins will contain two elements, the bin which x0 resides, and the bin in which x1 resides
    search_bins = []

    #determine in which bin x0 resides
    if x0 <= dims[0]:
        search_bins.append(0)
    else:
        for i in range(1,len(dims)):
            if dims[i-1] < x0 <= dims[i]:
                search_bins.append(i)
                break
    
    #determine in which bin x1 resides
    if x1 <= dims[0]:
        search_bins.append(0)
    else:
        for i in range(1,len(dims)):
            if dims[i-1] < x1 <= dims[i]:
                search_bins.append(i)
                break
           
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
    
    #get a list of the dimension partition points
    dims = []
    for i in range(1,len(bins)+1):
        dims.append(i/float(len(bins)))
    
    #search_bins will contain four elements, the bins in which x0,x1,y0,y1 reside, in that order
    search_bins = []
    
    #determine in which bin x0 resides
    if x0 <= dims[0]:
        search_bins.append(0)
    else:
        for i in range(1,len(dims)):
            if dims[i-1] < x0 <= dims[i]:
                search_bins.append(i)
                break
            
    #determine in which bin x1 resides
    if x1 <= dims[0]:
        search_bins.append(0)
    else:
        for i in range(1,len(dims)):
            if dims[i-1] < x1 <= dims[i]:
                search_bins.append(i)
                break
          
    #determine in which bin y0 resides
    if y0 <= dims[0]:
        search_bins.append(0)
    else:
        for i in range(1,len(dims)):
            if dims[i-1] < y0 <= dims[i]:
                search_bins.append(i)
                break
        
    #determine in which bin y1 resides
    if y1 <= dims[0]:
        search_bins.append(0)
    else:
        for i in range(1,len(dims)):
            if dims[i-1] < y1 <= dims[i]:
                search_bins.append(i)
                break

    #search from x0's bin to x1's bin
    for i in range(search_bins[0],search_bins[1]+1):
        for k in range(search_bins[2],search_bins[3]+1):
            for j in bins[i][k]:
                if x0 <= j[0] <= x1 and y0 <= j[1] <= y1:
                    count += 1
    
    return count 