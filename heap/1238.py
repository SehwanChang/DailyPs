import sys, heapq
input = sys.stdin.readline
inf = float('inf')
n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m) :
    a, b, w = map(int, input().split())
    graph[a].append((b,w))


def cal_dist(start) :
    q = []
    distance = [inf] * (n + 1)
    distance[start] = 0
    heapq.heappush(q,(0, start))

    while q :
        dist, node = heapq.heappop(q)
        if distance[node] < dist :
            continue
        for adjenct_node, weight  in graph[node] :
            cost = dist + weight
            if cost < distance[adjenct_node] :
                distance[adjenct_node] = cost
                heapq.heappush(q,(cost, adjenct_node))
    return distance

res = 0
end = cal_dist(x)
for i in range(1, n + 1) :
    start = cal_dist(i)
    res = max(res, start[x] + end[i])

print(res)