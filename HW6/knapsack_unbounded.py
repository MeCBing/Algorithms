def opt(number, input, dic):
    if number < min(input)[0]:
        list0 = [0 for n in input]
        dic.update( { number : (0, list0) } )
    else:
        ans = []
        for n in input:
            if number-n[0] not in dic:
                if number-n[0] >= 0:
                    a = opt(number-n[0], input, dic)
                    ans.append(a[0] + n[1])
                else:
                    ans.append(0)
            else:
                ans.append(dic[number-n[0]][0] + n[1])
        i, j = max(enumerate(ans), key= lambda x : x[1])
        c = dic[number-input[i][0]][1]
        d = [n for n in c]
        d[i] += 1
        dic.update( { number : (j, d)} )
    return dic[number]

def best(total_weight, input):
    back = {}

    def opt1(number, dic):
        if number < min(input)[0]:
            dic.update( { number : 0 } )
        else:
            max1 = (0, 0)
            for i, n in enumerate(input):
                if number-n[0] >= 0:
                    if number-n[0] not in dic:
                        opt1(number-n[0], dic) 
                    if max1[1] < (dic[number-n[0]] + n[1]):
                        max1 = (i, dic[number-n[0]] + n[1])    
            #print(max1)
            if number not in back:
                back[number] = []
            if (number-input[max1[0]][0]) not in back:
                back[number-input[max1[0]][0]] = []
            back[number] += [number-input[max1[0]][0]], max1[0]
            dic.update( { number : max1[1] } )
        return dic[number]

    def solution(input, total_weight):
        ans = [0 for n in input]
        while back[total_weight] != []:
            if back[total_weight][0][0] in back:
                ans[back[total_weight][1]] += 1
                total_weight = back[total_weight][0][0]
        return ans

    return opt1(total_weight, {}), solution(input, total_weight)

def solution1(back, i, w):
    ans = [0 for n in range(i)]
    k = w
    while k != 0:
        ans[back[k][1]] += 1
        k = back[k][0]
    return ans

def opt2(i, w, input):
    check = {}
    back = {}
    for wn in range(w+1):
        max1 = (0, 0, 0)
        for j in range(len(input)):
            if input[j][0] <= wn:
                a = check[wn-input[j][0]] + input[j][1]
                if a > max1[1]:
                    max1 = (j, a, wn-input[j][0])
        check[wn] = max1[1]
        back[wn] = (max1[2], max1[0])
    return check[w], solution1(back, i, w)

def best1(total_weight, input):
    return opt2(len(input), total_weight, input)

#best1(30, [(5, 9), (9, 18), (6, 12)])
#best(3, [(2, 4), (3, 5)])       #(5, [0, 1])
#best(30, [(5, 9), (9, 18), (6, 12)])
#best(3, [(1, 5), (1, 5)])       #(15, [3, 0])
#best(3, [(1, 2), (1, 5)])       #(15, [0, 3])
#best(3, [(1, 2), (2, 5)])       #(7, [1, 1])
#best1(58, [(5, 9), (9, 18), (6, 12)])    #(114, [2, 4, 2])
#best1(92, [(8, 9), (9, 10), (10, 12), (5, 6)])   #(109, [1, 1, 7, 1])
#print(back)