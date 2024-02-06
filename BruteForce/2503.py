import sys
from itertools import *
input = sys.stdin.readline
n = int(input())
candidate = list(permutations(range(1, 10) , 3))

for _ in range(n) :
    num, s, b = map(int, input().split())
    num = list(map(int, str(num)))
    new_candidate = []
    for c in candidate :
        strike, ball = 0, 0
        for i in range(3) :
            if c[i] == num[i] : 
                strike += 1
        for j in range(3) :
            if c[j] in num and c[j] != num[j]: 
                ball += 1
        if strike == s and ball == b :
            new_candidate.append(c)
    candidate = new_candidate  
print(len(candidate))