def opt(number, input, dic):
    if number < min(input)[0]:
        list0 = [0 for n in input]
        dic.update( { number : (0, list0) } )
    else:
        ans = []
        for i, n in enumerate(input):
                if number-n[0] >= 0:
                    if number-n[0] not in dic:
                        opt(number-n[0], input, dic)
                    #print(dic)
                    if dic[number-n[0]][1][i] < n[2]:
                        ans.append(dic[number-n[0]][0] + n[1])
                    else:
                        ans.append(dic[number-n[0]][0])
                else:
                    ans.append(0)
        #print(ans)
        i, j = max(enumerate(ans), key= lambda x : x[1])
        c = dic[number-input[i][0]][1]
        d = [n for n in c]
        if d[i] < input[i][2]:
            d[i] += 1
        dic.update( { number : (j, d)} )
        #print(number)
        #print(dic[number])
        #print(dic)
    return dic[number]


a = []
def best1(total_weight, input):
    a = [n[2] for n in input]
    print(a)
    back = {}

    def opt1(number, input, dic, a):
        if number < min(input)[0]:
            dic.update( { number : 0 } )
        else:
            #b = [n for n in a]
            #max = 0
            ans = []
            for i, n in enumerate(input):
                    if number-n[0] >= 0:
                        if number-n[0] not in dic:
                            opt1(number-n[0], input, dic, a)
                        #print(dic)
                        if a[i] > 0:
                            ans.append(dic[number-n[0]] + n[1])
                        else:
                            ans.append(dic[number-n[0]])
                    else:
                        ans.append(0)

            i, j = max(enumerate(ans), key= lambda x : x[1])
            if number not in back:
                back[number] = []
            if (number-input[i][0]) not in back:
                back[number-input[i][0]] = []
            a[i] -= 1
            print(a)
            back[number] += [number-input[i][0]], i
            dic.update( { number : j } )
        return dic[number]

    def solution(input, total_weight):
        ans = [0 for n in input]
        while back[total_weight] != []:
            if back[total_weight][0][0] in back:
                ans[back[total_weight][1]] += 1
                total_weight = back[total_weight][0][0]
        return ans
    return opt1(total_weight, input, {}, a), solution(input, total_weight)

def solution1(back, i, w, input):
    print(back)
    ans = [0 for n in range(i)]
    k = w
    t = i-1
    while back[k][t][0] != 0 or back[w][t][0] == 0:
        #print(k)
        if k == back[k][t][0] or ans[back[k][t][1]] == input[t][2]:
            t -= 1
        a = input[back[k][t][1]][0]
        b = (k - back[k][t][0])//a
        #print(b)
        for n in range(b):
            ans[back[k][t][1]] += 1
        
        #print(ans)
        k = back[k][t][0]
    return ans

def opt2(i, w, input):
    check = {}
    back = {}
    for wn in range(w+1):
        
        for j in range(len(input)):
            max1 = (0, 0, 0)
            k = min(wn//input[j][0], input[j][2])
            #print(k)
            for l in range(k+1):
                if input[j][0] <= wn:
                    if j != 0:
                        a = check[wn - (l * input[j][0])][j-1] + (l * input[j][1])
                    else:
                        a = 0 + (l * input[j][1])
                    if a > max1[1]:
                        max1 = (j, a, wn-(l *input[j][0]))
                else:
                    break
            #print(max1)        
            if j != 0:
                if check[wn][j-1] > max1[1]:
                    max1 = (j, check[wn][j-1], wn)
            if wn not in check:
                check[wn] = [max1[1]] 
                back[wn] = [(max1[2], max1[0])]
            else:
                check[wn].append(max1[1])
                back[wn].append((max1[2], max1[0]))
            
    return check[w][len(input)-1], solution1(back, i, w, input)

def best(total_weight, input):
    return opt2(len(input), total_weight, input)


#best(3, [(2, 4, 2),(3, 5, 3)])      #(5, [0, 1])
#best(3, [(1, 5, 2), (1, 5, 3)])     #(15, [2, 1])
#best(3, [(1, 5, 1), (1, 5, 3)])     #(15, [1, 2])
#best(20, [(1, 10, 6), (3, 15, 4), (2, 10, 3)])      #(130, [6, 4, 1])
#best(92, [(1, 6, 6), (6, 15, 7), (8, 9, 8), (2, 4, 7), (2, 20, 2)])     #(236, [6, 7, 3, 7, 2])