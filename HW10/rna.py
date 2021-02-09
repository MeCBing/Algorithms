from collections import defaultdict
import heapq

def best(input):

    n_len = len(input)
    check = {'AU', 'UA', 'GC', 'CG', 'GU', 'UG'}
    opt = defaultdict(int)
    back = {}
    
    def solution(i, j):
        if i > j:
            return ''
        if i == j:
            return '.'
        if (i,j) not in back:
            ans = ''
            for _ in range(i, j+1):
                ans += '.'
            return ans
        if back[i,j] == -1:
            return solution(i, j-1) + '.'
        else:
            return solution(i, back[i,j] - 1) + '(' + solution(back[i,j] + 1, j-1) + ')'

    def _best(i, j):  
        if i >= j or (i,j) in opt:
            return

        for a, u in enumerate(input[i:j], i):
            if u+input[j] in check:
                _best(i, a-1)
                _best(a+1, j-1)
                if opt[i, a-1] + opt[a+1, j-1] + 1 > opt[i,j]:
                    opt[i,j] = opt[i, a-1] + opt[a+1, j-1] + 1
                    back[i,j] = a

        _best(i, j-1)

        if opt[i, j-1] > opt[i,j]:
            opt[i,j] = opt[i, j-1]
            back[i,j] = -1

    _best(0, n_len-1)

    return opt[0, n_len-1], solution(0, n_len-1)

def total(input):

    n_len = len(input)
    check = {'AU', 'UA', 'GC', 'CG', 'GU', 'UG'}
    count_number = defaultdict(lambda : 1)

    def _best1(i, j):  
        if i >= j or (i,j) in count_number:
            return 

        s = 0

        for a, u in  enumerate(input[i:j], i):
            if u+input[j] in check: 
                _best1(i, a-1)
                _best1(a+1, j-1)
                s += (count_number[i, a-1] * count_number[a+1, j-1])

        _best1(i, j-1)
        s += count_number[i, j-1]
        count_number[i,j] = s

        return count_number[i,j]

    return _best1(0, n_len-1)

def kbest(input, k):

    n_len = len(input)
    check = {'AU', 'UA', 'GC', 'CG', 'GU', 'UG'}
    string = defaultdict(list)

    def k_best(i, j):  

        def trypush(q, ai, aj):
            if ai < len(string[i, q-1]) and aj < len(string[q+1, j-1]) and ((q, ai, aj) not in used):
                heapq.heappush(h, (-(string[i, q-1][ai][0] + string[q+1, j-1][aj][0] + 1), q, ai, aj))
                used.add((q, ai, aj))

        if i >= j:
            string[i, j] = [(0, '' if i != j else '.')]
            return

        if (i,j) in string:
            return 

        #new_list = [n for n in enumerate(input[i:j], i) if n[1] + input[j] in check]
        h = []
        used = set()

        for a, u in enumerate(input[i:j], i):
            if u+input[j] in check:
                k_best(i, a-1)
                k_best(a+1, j-1)
                h += [(-(string[i, a-1][0][0] + string[a+1, j-1][0][0] + 1), a, 0, 0)]
                used.add((a, 0, 0))

        k_best(i, j-1)
        h += [(-(string[i, j-1][0][0]), -1, 0, 0)]

        heapq.heapify(h)

        while len(string[i,j]) < k and h != []:
            ans1, l, ai, aj = heapq.heappop(h)
            if l != -1:
                string[i,j] += [(-ans1, string[i, l-1][ai][1] + '(' + string[l+1, j-1][aj][1] + ')')]
                trypush(l, ai+1, aj)
                trypush(l, ai, aj+1)
            else:
                string[i,j] += [(-ans1, string[i, j-1][ai][1] + '.')]
                if ai+1 < len(string[i, j-1]):
                    heapq.heappush(h, (-(string[i, j-1][ai+1][0]), l, ai+1, aj))

    k_best(0, n_len-1)
    return string[0, n_len-1]

def kbest1(input, k):

    n_len = len(input)
    check = {'AU', 'UA', 'GC', 'CG', 'GU', 'UG'}
    string = defaultdict(lambda : [0])
    back = defaultdict(list)

    def solution(i, j, k):
        if i > j:
            return ''
        if i == j:
            return '.'
        if (i,j) not in back:
            ans = ''
            for _ in range(i, j+1):
                ans += '.'
            return ans
        if back[i,j][k][0] == -1:
            return solution(i, j-1, back[i,j][k][1]) + '.'
        else:
            return solution(i, back[i,j][k][0] - 1, back[i,j][k][1]) + '(' + solution(back[i,j][k][0] + 1, j-1, back[i,j][k][2]) + ')'

    def k_best(i, j):  

        def trypush(q, ai, aj):
            if ai < len(string[i, q-1]) and aj < len(string[q+1, j-1]) and ((q, ai, aj) not in used):
                heapq.heappush(h, (-(string[i, q-1][ai] + string[q+1, j-1][aj] + 1), q, ai, aj))
                used.add((q, ai, aj))

        if i >= j or (i,j) in string:
            return

        h, used = [], set()

        for a, u in enumerate(input[i:j], i):
            if u+input[j] in check:
                k_best(i, a-1)
                k_best(a+1, j-1)
                h += [(-(string[i, a-1][0] + string[a+1, j-1][0] + 1), a, 0, 0)]
                used.add((a, 0, 0))

        k_best(i, j-1)
        h += [(-(string[i, j-1][0]), -1, 0, 0)]

        heapq.heapify(h)
        string[i,j] = []

        while len(string[i,j]) < k and h != []:
            ans1, l, ai, aj = heapq.heappop(h)
            string[i,j] += [-ans1]
            back[i, j] += [(l, ai, aj)]
            if l != -1:
                trypush(l, ai+1, aj)
                trypush(l, ai, aj+1)
            else:
                if ai+1 < len(string[i, j-1]):
                    heapq.heappush(h, (-(string[i, j-1][ai+1]), l, ai+1, aj))
                    
    k_best(0, n_len-1)

    return [(n, solution(0, n_len-1, i)) for i, n in enumerate(string[0, n_len-1])]

#kbest('GCACG', 20)
#total('CG')
#kbest('AUG', 2)
#kbest('AC', 2)
#best("AGGCAUCAAACCCUGCAUGGGAGCG")
#kbest1("AGGCAUCAAACCCUGCAUGGGAGCG",10)
#total("GAUGCCGUGUAGUCCAAAGACUUC")
#kbest('CG', 2)