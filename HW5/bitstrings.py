def non(number):
    dic = []
    for n in range(number):
        numberlist = []
        a = dic
        for i in a:
            numberlist.append(i + '1')
            numberlist.append(i + '0')
            
        if numberlist != []:
            dic = numberlist
        else:
            dic = ["1", "0"]
    return dic

def non_no(number):
    dic = []
    for n in range(number):
        numberlist = []
        a = dic
        for i in a:
            numberlist.append(i + '1')
            if i[-1] != '0':
                numberlist.append(i + '0')
            
        if numberlist != []:
            dic = numberlist
        else:
            dic = ["1", "0"]
    return len(dic)

def non_yes(number):
    dic = []
    for n in range(number):
        numberlist = []
        a = dic
        for i in a:
            if i[:2] != '01':
                if i[-2:] != '10':
                    if len(i) + 1 != number or '00' in i:
                        numberlist.append(i + '1')
                if len(i) + 1 != number or i[-1] != '1':
                    numberlist.append(i + '0')
                    
        if numberlist != []:
            dic = numberlist
        else:
            dic = ["1", "0"]
    return len(dic)
a = 5
non(a)
non_no(a)
non_yes(a)