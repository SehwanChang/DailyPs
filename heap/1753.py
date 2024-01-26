import sys, heapq
input = sys.stdin.readline
inf = float('inf')

V, E = map(int, input().split())
k = int(input())
graph = [[] for _ in range(V + 1)]
distance = [inf] * (V + 1)
for _ in range(E) :
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def search(start) :
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q :
        dist, node = heapq.heappop(q)
        if distance[node] < dist :
            continue

        for i in graph[node] :
            cost = dist + i[1]
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

search(k)
for i in range(1, V + 1) :
    if distance[i] == inf :
        print('INF')
    else :
        print(distance[i])