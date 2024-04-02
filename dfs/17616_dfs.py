import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
n, m , x = map(int, input().split())

def dfs(start, graph) :
    cnt = 1
    visited[start] = True
    for next in graph[start] :
        if not visited[next] :
            cnt += dfs(next, graph)
    return cnt
higher = [[] for _ in range(n + 1)]
lower = [[] for _ in range(n + 1)]

for _ in range(m) :
    high, low = map(int, input().split())
    higher[low].append(high)
    lower[high].append(low)

visited  = [False] * (n + 1)
top_rank = dfs(x, higher)
low_rank = n - dfs(x, lower)
print(top_rank, low_rank)
# 5 3 1
# 2 3
# 3 4
# 4 5
# 2 > 3 > 4 > 5 : 1 or 5 가능함.
