# MST : 사이클 없이 모든 노드(vertex) 연결, edge cost 합의 최솟값
# vertex = n 개 : edge 갯수 = n - 1
# cost 가 최소인 Edge 부터 MST 에 포함
# 시간 보갖ㅂ도 : O(ElogE)
# 1) cost 를 오름차순으로 정렬
# 2) cycle 형성하는지 검사 : union- find
# 3) 사이클 형성하지 않는 edge만 포함
import sys
input = sys.stdin.readline
v , e  = map(int,input().split())
parent = [i for i in range(v + 1)]
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

edges = []
total_cost = 0
for _ in range(e) :
    a, b, cost = map(int,input().split())
    edges.append((cost, a, b))
edges.sort()

for i in range(e) :
    cost, a, b = edges[i]
    if find_parent(parent, a) != find_parent(parent, b) :
        union_parent(parent, a, b)
        total_cost += cost
print(total_cost)