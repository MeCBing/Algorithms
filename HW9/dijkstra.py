#!/usr/bin/python3
from collections import defaultdict
from heapdict import heapdict

def solution(k, back):
    #print(back)
    n = 0
    ans = []
    while n != k:
        ans.append(n)
        n = back[n]
    return ans + [k]

def _shortest(node, input):

    dic_input = defaultdict(lambda : [])
    dic_node = defaultdict(lambda : float("inf"))
    brown_dic = heapdict()
    black = {}
    back = {}

    for i,j,x in input:
        dic_input[i].append((j,x))
        dic_input[j].append((i,x))

    if node-1 not in dic_input:
        return None
    #print(dic_input)
    dic_node[node-1] = 0
    brown_dic[node-1] = 0

    while len(brown_dic) != 0:
        a = brown_dic.popitem()
        
        black[a[0]] = a
        if a[0] == 0:
            #print(a[0])
            break
        b = [n for n in dic_input[a[0]] if n[0] not in black]
        #print(b)
        for i, j in b:
            if (dic_node[a[0]] + j) < dic_node[i]:
                dic_node[i] = dic_node[a[0]] + j
                brown_dic[i] = dic_node[i]
                back[i] = a[0]

    return (black[0][1], solution(node-1, back)) if 0 in back else None

def _solution(k, back):
    ans = [k]
    while k != 0:
        ans.append(back[k])
        k = back[k]
    return ans[::-1]

def shortest(node, input):

    dic_input = defaultdict(lambda : [])
    dic_node = defaultdict(lambda : float("inf"))
    brown_dic = heapdict()
    black = {}
    back = {}

    for i,j,x in input:
        dic_input[i].append((j,x))
        dic_input[j].append((i,x))

    if node-1 not in dic_input:
        return None
    #print(dic_input)
    dic_node[0] = 0
    brown_dic[0] = 0

    while len(brown_dic) != 0:
        a = brown_dic.popitem()
        
        black[a[0]] = a
        if a[0] == (node-1):
            #print(a[0])
            break
        b = [n for n in dic_input[a[0]] if n[0] not in black]
        #print(b)
        for i, j in b:
            if (dic_node[a[0]] + j) < dic_node[i]:
                dic_node[i] = dic_node[a[0]] + j
                brown_dic[i] = dic_node[i]
                back[i] = a[0]

    return (black[node-1][1], _solution(node-1, back)) if node-1 in back else None

def shortest1(end, path):
    map = [{} for i in range(end)]
    for i in path:
        map[i[0]][i[1]] = i[2]
        map[i[1]][i[0]] = i[2]
    h = heapdict()
    U = {}
    for i in range(1, end):
        U[i] = float('inf')
    source = [float('inf') for i in range(end)]
    shortlist = [0 for i in range(end)]
    point = 0
    shortpath = 0
    while(point != end-1):
        for j in map[point]:
            if(j in U):
                h[j] = map[point][j] + shortpath
        if(len(h) == 0):
            return None
        p = h.popitem()
        for j in map[p[0]]:
            if(p[1] == shortlist[j] + map[p[0]][j] and j not in U):
                source[p[0]] = j
                break
        U.pop(p[0])
        print(p[0],p[1])
        shortpath = p[1]
        point = p[0]
        shortlist[point] = shortpath

    SS = []
    pp = point
    SS.append(pp)
    while pp != 0:
        pp = source[pp]
        SS.append(pp)
    del p
    return shortpath,SS[::-1]

#shortest(4, [(0,1,1), (2,3,1)])
#shortest1(4, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)])
#   (4, [0,1,2,3])
#shortest(5, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)])
#   None
#shortest(4, [(0,1,1), (2,3,1)])
#   None