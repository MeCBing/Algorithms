#!/usr/bin/env python3

'''based on Rachel (sousar)'s code; minor edits by the instructor.'''

def best(W, a):
    def solution(i, w):
        if i <= 0:
            return []
        return solution(i-1, w-a[i-1][0]*back[w][i]) + [back[w][i]] # 0-based in a

    dp = [[0 for i in range(len(a)+1)] for j in range(W+1)]
    back = [[0 for i in range(len(a)+1)] for j in range(W+1)]
    for i, (weight, value, count) in enumerate(a, 1): # 1-based in dp/back
        for w in range(1, W+1):
            for j in range(min(count, w//weight)+1):
                v = dp[w - j*weight][i-1] + j*value
                if dp[w][i] < v:
                    dp[w][i] = v
                    back[w][i] = j
    return dp[W][len(a)], solution(len(a), W)

#Correct, 0.000 s
#Correct, 0.000 s
#Correct, 0.000 s
#Correct, 0.000 s
#Correct, 0.003 s
#Correct, 0.010 s
#Correct, 0.009 s
#Correct, 0.007 s
#Correct, 0.005 s
#Correct, 0.086 s
