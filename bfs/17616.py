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
    #시작 노드 : 계산에서 제외하려고
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
    high, low = map(int, input().split())
    # 나보다 더 잘한사람수 세기 -> 최소 랭크
    higher[low].append(high)
    # 나보다 더 못한사람수 세기 -> 최대 랭크
    lower[high].append(low)

# 5명중에 2명이 나보다 잘함: 나의 최소 순위 = 3위
high_rank = 1 + bfs(x , higher)

#5명중에 1명이 나보다 못한 경우 나의 최대순위 = 2위
low_rank = n - bfs(x, lower)

print(high_rank, low_rank)

# 5 3 1
# 2 3
# 3 4
# 4 5
# 2 > 3 > 4 > 5 : 1 or 5 가능함.
