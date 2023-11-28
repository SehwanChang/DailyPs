import sys
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

v, e = map(int,input().split())
parent = [i for i in range(v + 1)]
edges = []
for i in range(e) :
    a, b, cost = map(int,input().split())
    edges.append((cost, a, b))
edges.sort()
total_cost = 0
max_edge = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b) :
        union_parent(parent, a, b)
        total_cost += cost
        max_edge = max(cost, max_edge)
print(total_cost - max_edge)
