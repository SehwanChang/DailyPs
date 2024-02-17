import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * m for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y) :
    if x == n - 1 and y == m - 1:
        return 1
    if dp[x][y] !=  -1 :
        return dp[x][y]
    
    way = 0
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m :
            if graph[x][y] > graph[nx][ny] :
                way += dfs(nx, ny)
    dp[x][y] = way
    return dp[x][y]

print(dfs(0, 0))


# 4 5
# 50 45 37 32 30
# 35 50 40 20 25
# 30 30 25 17 28
# 27 24 22 15 10
# 3