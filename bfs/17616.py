import sys
from collections import deque
input = sys.stdin.readline
n, m , x = map(int, input().split())
higher = [[] for _ in range(n + 1)]
lower = [[] for _ in range(n + 1)]
for _ in range(m) :
    a, b = map(int, input().split())
    lower[a].append(b)
    higher[b].append(a)

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
high_rank = 1 + bfs(x , higher)
low_rank = n - bfs(x, lower)

print(high_rank, low_rank)

# 5 3 1
# 2 3
# 3 4
# 4 5

# 1번 노드 직접적으로 달성 x : 역방향 추적.

# 2 > 3 > 4 > 5 : 1 or 5 가능함.

# 5 5 1
# 1 3
# 2 3
# 3 4
# 3 5
# 4 5

# 3 > 4 > 5 : 1 or 2 가능함


# 5 3 1
# 2 4
# 3 1
# 2 3
# 5 2 3 4 1
# 2 3 1 4
# 2 3 4 1