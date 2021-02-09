def bsts(number):
    if number < 0:
        return None
    dic = { 0: 1, 1: 1}
    for n in range(2, number+1):
        count = 0
        for i in range(1, n+1):
            count += dic[i-1] * dic[n-i]
        dic.update( { n : count } )
    return dic[number]

"""def ans():
    for n in range(10+1):
        ans = bsts(n)
        print(ans)
    #pass
ans()"""

#bsts(5)
#bsts(3)
#bsts(2)
#bsts(1)