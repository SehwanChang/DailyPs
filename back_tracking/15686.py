import sys
input = sys.stdin.readline
from itertools import *

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
chickens = []
houses = []

for i in range(n) :
    for j in range(n) :
        if graph[i][j] == 1 :
            houses.append((i, j))
            continue
        elif graph[i][j] == 2: 
            chickens.append((i, j))

min_distance = float('inf')
for chicken in combinations(chickens, m) :
    chicken_len = 0
    for house in houses : 
        tmp = 10000
        for i in range(m) :
            tmp = min(tmp, abs(house[0] - chicken[i][0]) + abs(house[1] - chicken[i][1]))
        chicken_len += tmp
    min_distance = min(chicken_len, min_distance)
print(min_distance) 