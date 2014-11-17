# Performs search in unsorted L.
# L might not be sorted. Can't use sorting to solve this.
def searchGreaterNotSorted(L, v):
    
    n = 0
    for l in L:
        if l > v:
            n += 1 
    return n


# Performs search in sorted L (ascending order).
# L is sorted.
def searchGreaterSorted(L, v):
    
    #t = None
    for ind,val in enumerate(L):
        #if L[i] != t:
        if val > v:
            return len(L[ind:])
        #t = L[i]

    return 0

# Performs binary search in sorted L (ascending order).             
#def searchGreaterBinSearch(L, v):
            
#    if v >= L[-1]:
#        return 0
    
#    low = 0
#    high = len(L) - 1
#    mid = low + ((high - low)/2)
    
#    while low <= high:
#        mid = low + ((high - low)/2)
#        if L[mid] == v:
#            for i in range(mid,len(L)):
#                if L[i] > v:
#                    return len(L[i:])
#            return 0
#        elif L[mid] > v:
#            high = mid - 1
#        else:
#            low = mid + 1
#    return len(L[mid:])

def searchGreaterBinSearch(L, v):
    
    low = 0
    high = len(L)
    mid = low + ((high - low)/2)
    
    while low < high:
        mid = low + ((high - low)/2)
        if L[mid] == v:
            while L[mid] == v:
                mid += 1
                if mid == len(L):
                    return 0
            return len(L[mid:])
        elif L[mid] > v:
            high = mid 
        else:
            low = mid + 1
    
    if L[mid] < v:
        return len(L[mid+1:])
    else:
        return len(L[mid:])


# Performs range search in sorted L (ascending order).
def searchInRange(L, v1, v2):
        
    return(searchGreaterBinSearch(L,v1) - searchGreaterBinSearch(L,v2))

#v1 = 2
#v2 = 11
#print searchInRange(L, v1, v2)