import heapq

def merge(input):
    #print(input)
    l = len(input)
    lon = 0
    pointindex = [0 for n in input]
    compare = []
    ans = []
    for n in range(l):
        heapq.heappush(compare, input[n][pointindex[n]])
        lon += len(input[n])
    
    while len(ans) < lon:
        i = 0
        while i < l:
            if pointindex[i] < len(input[i]):    
                if compare[0] == input[i][pointindex[i]]:
                    pointindex[i] += 1
                    ans.append(compare[0])
                    if pointindex[i] == len(input[i]):
                        heapq.heappop(compare)
                        pointindex[i] = float("inf")
                    elif pointindex[i] != float("inf"):
                        heapq.heapreplace(compare, input[i][pointindex[i]])
                    break
            i += 1
    return ans

def kmergesort(input, k):
    if len(input) == 1:
        return input
    if len(input) < k:
        return merge([[n] for n in input])
    ans = []
    l = len(input)
    if(l%k == 0):
        index = l//k
    else:
        index = l//k + 1
    firstindex = 0
    for n in range(1,k+1):
        #print(input[firstindex:firstindex+index])
        ans.append(kmergesort(input[firstindex:firstindex+index], k))
        firstindex = index * n
    #anslist = merge(ans)
    return merge(ans)

#merge([[4,8],[1,2],[3,5]])

#kmergesort([4,1,5,2,6,3,7,0], 3)  # k=3 [0,1,2,3,4,5,6,7]
#kmergesort(range(100), 4)
#kmergesort([4,1,5,2,6,3,7,0,8], 3)