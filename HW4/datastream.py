import heapq

def _maxheap(input, lenth, index):
    if 2*index+2 < lenth:
        if input[(2*index)+1] < input[(2*index)+2]:
            if input[index] < input[(2*index)+2]:
                input[index],input[(2*index)+2] = input[(2*index)+2], input[index]
                _maxheap(input, lenth, (2*index)+2)
        if input[(2*index)+1] >= input[(2*index)+2]:
            if input[index] < input[(2*index)+1]:
                input[index],input[(2*index)+1] = input[(2*index)+1], input[index]
                _maxheap(input, lenth, (2*index)+1)
    if 2*index+2 == lenth:
        if input[index] < input[(2*index)+1]:
                input[index],input[(2*index)+1] = input[(2*index)+1], input[index]
                _maxheap(input, lenth, (2*index)+1)

def ksmallest(number, input):
    heap = [n for n in input[:number]]

    for n in range(len(heap), -1, -1):
        _maxheap(heap, len(heap), n)
    for n in input[number:]:
        if n < heap[0]:
            heap[0] = n
            _maxheap(heap, len(heap), 0)
    """for n in range(len(heap)-1, 0, -1):
        heap[0], heap[n] = heap[n], heap[0]
        _maxheap(heap, n, 0)"""
    heap.sort()
    
    return heap 

#ksmallest(4, [10, 2, 9, 3, 7, 8, 11, 5, 7]) # [2, 3, 5, 7]
#ksmallest(6, [9, 7, 8, 11, 5, 10, 3, 2, 1])
#ksmallest(6, [10, 2, 9, 3, 7, 8, 11, 9, 3, 7, 8, 11, 8, 11, 5, 7]) # [2, 3, 3, 5, 7, 7]
#ksmallest(3, range(1000000, 0, -1)) # [1, 2, 3]
def _ksmallest(number, input):
    ansd = []
    for i, n in enumerate(input):
        if i < number:
            heapq.heappush(ansd, n)
        else:
            j = max((b, a) for a, b in enumerate(ansd))
            if n < j[0]:
                ansd[0], ansd[j[1]] = ansd[j[1]], ansd[0]
                heapq.heapreplace(ansd, n) 
    ansd.sort()
    return ansd

#ksmallest(4, [10, 2, 9, 3, 7, 8, 11, 5, 7])