from collections import defaultdict

def order_top_down(Howmany_Node, input):
    a = {0}
    for n in range(10,0,-1):
        print(n)
        a.add(n)
    print(a)
    return 0

order_top_down(1,1)

def order1(Howmany_Node, input):    
    if input == []:
        return [n for n in range(Howmany_Node)]
    list_of_node, dic = [0] * Howmany_Node, defaultdict(lambda : [])
    for u, v in input:
        dic[u].append(v)
        list_of_node[v] += 1
    list_of_edges = [i for i, n in enumerate(list_of_node) if n == 0]
    if list_of_edges == []:
        return None
    n = 0
    while n < len(list_of_edges):
        a = dic[list_of_edges[n]]
        for x in a:
            list_of_node[x] -= 1
            if list_of_node[x] == 0:
                list_of_edges.append(x)
        n += 1    
    return list_of_edges if all([ n == 0 for n in list_of_node]) else None 

def order(HowmanyNode, input):    
    if input == []:
        return [n for n in range(HowmanyNode)]
    list_of_node, dic, list_of_answer = [0] * HowmanyNode, defaultdict(lambda : []), []
    for n in input:
        dic[n[0]].append(n)
        list_of_node[n[1]] += 1
    list_of_edges = [i for i, n in enumerate(list_of_node) if n == 0]
    if list_of_edges == []:
        return None
    while list_of_edges != []:
        n = list_of_edges[0]
        a = dic[n]
        list_of_edges.pop(0)
        list_of_answer.append(n)
        for x in a:
            list_of_node[x[1]] -= 1
            if list_of_node[x[1]] == 0:
                list_of_edges.append(x[1])
            
    return list_of_answer if all([ n == 0 for n in list_of_node]) else None 

order1(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)])
#   [0, 1, 2, 3, 4, 5, 6, 7]
#order1(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)])
#   [0, 1, 2, 4, 3, 5, 6, 7]
#order1(14, [(0,1), (1,2), (2,1), (2,3)])
#   None
#order1(5, [(0,1), (1,2), (2,3), (3,4)])
#   [0, 1, 2, 3, 4]
#order1(5, [])
#   [0, 1, 2, 3, 4]  # could be any order  
#order1(3, [(1,2), (2,1)])
#   None
#order1(1, [(0,0)]) # self-loop
#   None