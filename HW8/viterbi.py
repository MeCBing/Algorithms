from collections import defaultdict
def _path(back, n):
    ans = []
    while n != None:
        ans.append(n)
        n = back[n]
    return ans[::-1]

def longest(How_many_Node, input):    
    if input == []:
        return (0, [])

    list_of_node, dic, dic1 = [0] * How_many_Node, defaultdict(lambda : []), defaultdict(lambda : [])

    for u, v in input:
        dic[u].append(v)
        dic1[v].append(u)
        list_of_node[v] += 1

    list_of_edges = [i for i, n in enumerate(list_of_node) if n == 0 and i in dic]

    if list_of_edges == []:
        return (0, [])
    
    dic2 = defaultdict(int) #{i : 0 for i, n in enumerate(list_of_node) if n == 0}

    n = 0
    while n < len(list_of_edges):
        a = dic[list_of_edges[n]]
        for x in a:
            list_of_node[x] -= 1
            if list_of_node[x] == 0:
                list_of_edges.append(x)
        n += 1    

    back = {}
    if all([ n == 0 for n in list_of_node]):
        for n in list_of_edges:
            a = dic1[n]
            if a != []:
                ans = max([(dic2[y], y) for y in a], key = lambda x: min(x))
            else:
                ans = (-1, None)
            dic2[n] = ans[0] + 1
            back[n] = ans[1]
        answer = max(dic2, key= (lambda x: dic2[x]))
        return dic2[answer], _path(back, answer)
    else:
        return (0, [])
    
    """final = [n for n in range(How_many_Node) if n not in dic]
    start = {i : 0 for i, n in enumerate(list_of_node) if n == 0}

    back = defaultdict(lambda : {})
    def _longest(k, di, i):
        if k not in di:
            a = dic1[k]
            ans = max([(_longest(n[0], di, i), n[0]) for n in a], key = lambda x: min(x))
            back[i][k] = ans[1]
            di[k] = ans[0] + 1
        return di[k]
    def _path(i, final):
        #print(back[i])
        n = final
        ans = [final]
        while n in back[i]:
            ans.append(back[i][n])
            n = back[i][n]
            while n not in back[i] and i != 0:
                i -=1
        return ans[::-1]
    return max([(_longest(x, start, i), _path(i, x)) for i, x in enumerate(final)], key= lambda x: min(x[1])) if final != [] else (None, [])"""

#judge(20000, tuples[:100], 2)

longest(10, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)])
#   (5, [0, 2, 3, 4, 5, 6])
#longest(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)])
#   (5, [0, 2, 4, 3, 5, 6]) 
#longest(8, [(0,1), (0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7), (6,7)])
#   (7, [0, 1, 2, 4, 3, 5, 6, 7])  # unique answer