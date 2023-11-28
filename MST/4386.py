import sys, math
input = sys.stdin.readline
def find_parent(parent, x) :
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
def union_parent(parent, a, b) :
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b : 
        parent[b] = a
    else : 
        parent[a] = b
n = int(input())
parent = [i for i in range(n + 1)]
coord = []
for i in range(n) :
    x, y = map(float,input().split())
    coord.append((x, y))
edges = []
for i in range(n) :
    x1, y1 = coord[i]
    for j in range(i + 1, n) :
        x2, y2 = coord[j]
        edges.append((math.sqrt((x1 - x2)**2 + (y1 - y2)**2), i, j))
edges.sort()
total_cost = 0
for edge in edges : 
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b) :
        union_parent(parent, a, b)
        total_cost += cost
print(round(total_cost, 2))