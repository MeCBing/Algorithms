import os
def _max_wis_bottomup(input):
    max_a, max_b = (0, []), (0, [])
    for f in range(len(input)):
        a = max_a
        b = max_b
        na = input[f] + a[0]
        if na > b[0]:
            max_a = max_b
            max_b = ( na, a[1] + [input[f]] )
        else:
            max_a = max_b
            max_b = ( b[0], b[1] )
    return max(max_a, max_b)

def _max_wis_topdown_1(input, number):
    if number < 0:
        dic = {-1 : (0, []), -2 : (0, [])}
    if number >= 0:
        b = _max_wis_topdown_1(input, number-1)
        dic = b
        print(dic)
        if number-2 in b:
            a = b
        else:
            a = _max_wis_topdown_1(input, number-2)
        na = input[number] + a[number-2][0]
        if na> b[number-1][0]:
            dic.update( { number : ( na, a[number-2][1] + [input[number]] ) } )
        else:
            dic.update( { number : (b[number-1][0], b[number-1][1]) } )
    return dic

def _max_wis_topdown_2(input, number, dic=None):
    if dic == None:
        dic = {-1 : (0, []), -2 : (0, [])}
    if number >= 0:
        #print(-1 in dic)
        #print(number)
        #print(dic)
        #a = {}
        if number-2 in dic:
            #print("number-2")
            a = dic
        else:
            a = _max_wis_topdown_2(input, number-2, dic)
        if number-1 in dic:
            #print("number-1")
            b = dic
        else:
            b = _max_wis_topdown_2(input, number-1, a)
        na = input[number] + a[number-2][0]
        if na> b[number-1][0]:
            dic.update( { number : ( na, a[number-2][1] + [input[number]] ) } )
        else:
            dic.update( { number : (b[number-1][0], b[number-1][1]) } )
            #os.system("pause")
    return dic
    
def max_wis(input):    
    return _max_wis_topdown_2(input,len(input)-1)[len(input)-1]

#max_wis([7,8,5])        #(12, [7, 5])
#max_wis([-1,8,10])      #(10, [10])
#max_wis([])             #(0, [])
#max_wis([-5, -1, -4])   #(0, [])
#max_wis([63229, 7871, 74587, 59445, 71381, 5404, 56721, 41863, 62960, 42424, 37376, 38654, 9686, 88564, 71093, 69118, 26876, 44293, 48730, 2476, 58586, 23466, 4192, 48799, 15818, 28847, 82565, 71941, 95094, 64294, 79614, 16219, 16348, 37528, 57940, 73917, 31890, 80693, 88456, 82255, 39260, 8070, 36726, 87408, 44400, 85485, 88349, 45095, 66399, 12786, 99639, 19331, 63101, 72119, 20801, 69561, 33307, 66400, 9388, 41212, 63564, 85236, 72617, 4787, 97918, 32153, 58247, 8466, 68896, 93322, 21028, 18211, 55043, 24187, 13768, 17505, 54214, 71736, 5284, 41499, 87421, 42354, 64137, 77183, 31897, 40971, 94056, 85477, 17893, 95807, 77428, 13186, 51169, 48753, 36957, 27003, 78557, 93281, 84281, 99236]) #= (2969210, …)