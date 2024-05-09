from itertools import combinations
import sys
input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
nums = [i for i in range(n)]
tmp = float('inf')
for i in range(1, n + 1):
    for comb in combinations(nums, i):
        tmp_s, tmp_b = 1, 0
        for idx in comb:
            tmp_s *= graph[idx][0]
            tmp_b += graph[idx][1]
        tmp = min(tmp, abs(tmp_b - tmp_s))
print(tmp)


# 신맛 : 곱, 쓴맛: 합
