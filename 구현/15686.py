from itertools import combinations
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
house = []
chicken = []
for i in range(n) :
    for j in range(n) :
        if graph[i][j] == 1 :
            house.append((i, j))
        elif graph[i][j] == 2 :
            chicken.append((i, j))

min_distance = float('inf')
for comb in combinations(chicken, m) :
    chicken_len = 0
    for h in house :
        tmp = 10000
        for j in range(m) :
            tmp = min(tmp, abs(h[0] - comb[j][0]) + abs(h[1] - comb[j][1]))
        chicken_len += tmp
    min_distance = min(min_distance, chicken_len)
print(min_distance)
# print(house)
# print(chicken)