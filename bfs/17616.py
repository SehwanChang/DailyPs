import sys
from collections import deque
input = sys.stdin.readline
n, m , x = map(int, input().split())
higher = [[] for _ in range(n + 1)]
lower = [[] for _ in range(n + 1)]

def bfs(start, graph) :
    q = deque()
    visited = [False] * (n + 1)
    visited[start] = True
    q.append(start)
    rank = -1
    while q :
        cur = q.popleft()
        rank += 1
        for next in graph[cur] :
            if not visited[next] :
                visited[next] = True
                q.append(next)

    return rank

for _ in range(m) :
    a, b = map(int, input().split())
    lower[a].append(b)
    higher[b].append(a)

high_rank = 1 + bfs(x , higher)
low_rank = n - bfs(x, lower)

print(high_rank, low_rank)