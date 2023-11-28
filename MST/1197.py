#프림 알고리즘 : nlogn
#시작 노드만 MST 집합에 속함 
#트리 집합에 속한 정점 / 인접한 정점 중 낮은 가중치의 간선과 연결된 정점에 대해
#간선, 정점을 MST트리 집합에 넣음
#MST 집합의 원소 개수가 그래프 정점의 개수 될때까지 반복
from collections import defaultdict
import sys, heapq
input = sys.stdin.readline

mst = list()
graph = defaultdict(list)
selected_vertex = set()
v , e = map(int,input().split())
for edge in range(e) :
    src, dest, weight = map(int,input().split())
    graph[src].append((dest, weight))
    graph[dest].append((src, weight))
mst_graph = [[0] * v for _ in range(v)]
mst_nodes = [-1 for _ in range(v)]
visited = [True for _ in range(v)]

q = [(0, 1, 1)]
while q : 
    cost, node, prev = heapq.heappop(q)
    if visited[node - 1] == False :
        continue
    visited[node - 1] = False
    mst_graph[node - 1][prev - 1] = 1
    mst_graph[prev - 1][node - 1] = 1
    mst_nodes[node - 1] = cost
    for dst, weight in graph[node] :
        if visited[dst - 1] :
            heapq.heappush(q, (weight, dst, node))
    mst_graph[0][0] = 1
print(sum(mst_nodes))



