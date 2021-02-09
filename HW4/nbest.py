import heapq, random, time

def test():
    array = [n for n in range(100)]
    #print(array)
    #random.shuffle(array)
    t = time.time()
    
    for n in range(10000):
        
        heapq.heapify(array)
    print("heapify : ", time.time() - t)
    t = time.time()
    for n in range(10000):
        a = []
        random.shuffle(array)
        for x in array:
            heapq.heappush(a, x)
    print("heappush : ", time.time() - t)
    #print(array)
    array1 = [n for n in range(100)]
    array2 = array1[::-1]
    t = time.time()
    for n in range(10000):
        heapq.heapify(array1)
    print("sort heapify : ", time.time() - t)
    t = time.time()
    for n in range(10000):
        heapq.heapify(array2)
    print("reversely-sorted heapify : ", time.time() - t)
    t = time.time()
    for n in range(10000):
        a = []
        for x in array1:
            heapq.heappush(a, x)
    print("sort heappush : ", time.time() - t)
    t = time.time()
    for n in range(10000):
        a = []
        for x in array1:
            heapq.heappush(a, x)
    print("reversely-sort heappush : ", time.time() - t)
test()

def _nbesta(a, b):
    a.sort()
    b.sort()
    ans = []
    small = a[0] + b[0]
    k = small
    while len(ans) < len(a): 
        ls = []
        for i in b:
            if i > k:
                break
            for j in a:
                if i + j > k or j > k or len(ans) + len(ls) >= len(a):
                    break
                elif i + j == k:
                    ls.append((j, i))
        if len(ls) != 0:
            ans += ls
        k += 1    
    print(ans)
    return 0

def nbesta(a, b):
    ans = [(x,y) for x in a for y in b]
    #print(ans)
    return sorted(ans, key = lambda x: (x[0] + x[1], x[1]))[:len(a)]

def qselect(input, k):
    pivot = random.randint(0, len(input) - 1)
    print("pivot",input[pivot])
    left = [n for n in input if n[0] + n[1] < input[pivot][0] + input[pivot][1]]
    print("left", left)
    mid = [n for n in input if n[0] + n[1] == input[pivot][0] + input[pivot][1]]
    print("mid", mid)
    if len(left) == k:
        return left
    elif len(left) + len(mid) >= k:
        return left + mid
    else:
        right = [n for n in input if n[0] + n[1] > input[pivot][0] + input[pivot][1]]
        print("right", right)
        return left + mid + qselect(right, k-len(left)-len(mid))
    
    
def nbestb(a, b):
    ans = [(x, y) for x in a for y in b]
    nans = qselect(ans, len(a))
    return sorted(nans, key = lambda x: (x[0] + x[1], x[1]))[:len(a)]
    
def nbestc(a, b):
    a.sort()
    b.sort()
    ans = []
    checkheap = []
    i, j = 0, 0
    heapq.heappush(checkheap, (a[i]+b[j], i, j))
    while len(ans) < len(a):
        pop = heapq.heappop(checkheap)
        print(checkheap)
        ans.append((a[pop[2]],b[pop[1]]))
        i, j = pop[1], pop[2]
        heapq.heappush(checkheap, (a[i+1]+b[j], j, i+1))
        heapq.heappush(checkheap, (a[i]+b[j+1], j+1, i))

    return ans #sorted(ans, key = lambda x: (x[0] + x[1], x[1]))

a, b = [4, 1, 5, 3], [2, 6, 3, 4]
#ans = [(x,y) for x in a for y in b]
#heapq.heapify(ans)
#ans
nbestc(a, b)
nbestb(a, b)
nbesta(a, b)