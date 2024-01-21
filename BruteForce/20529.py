import sys
input = sys.stdin.readline
from itertools import combinations

def cal_dist(a, b) :
    cnt = 0
    for i, j in zip(a, b) :
        if i != j :
            cnt += 1
    return cnt

t = int(input())
for i in range(t): 
    n = int(input())
    mbti = list(input().split())
    if n > 32 :
        print(0)
        continue
    res = 13
    case = combinations(mbti, 3)
    for a, b, c in case :
        cnt = 0
        cnt += cal_dist(a, b)
        cnt += cal_dist(a, c)
        cnt += cal_dist(b, c)
        res = min(cnt, res)
    print(res)