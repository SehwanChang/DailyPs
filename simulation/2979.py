# 5 3 1
# 1 6 
# 3 5
# 2 8  : 33
# 5 * 1 * (2 - 1 + 8 - 6) + 3 * 2 * (5) + 1 * 3 *(5 - 3) = 33
# 1 - 2 , 6 - 8 : 혼자
# 2 - 3 , 

import sys
input = sys.stdin.readline
a, b, c = map(int,input().split())
time = [0] * 100
res = 0
for i in range(3) :
    start, end = map(int,input().split())
    for j in range(start, end) :
        time[j] += 1
for i in time:
    res += {0: 0, 1: a, 2: b * 2, 3: c * 3}[i]

print(res)