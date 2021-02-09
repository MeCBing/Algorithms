# number of BSTs; c.f. Catalan number

def bsts(n):
    num = {0:1}
    for i in range(1, n+1):
        num[i] = sum(num[j] * num[i-j-1] for j in range(i))
    return num[n]

if __name__ == "__main__":
    for i in range(10):
        print(i, bsts(i))
