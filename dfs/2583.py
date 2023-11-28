import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
m, n, k = map(int,input().split())
graph = [[0] * n for i in range(m)]

for i in range(k) :
    x1, y1, x2, y2= map(int,input().split())
    for x in range(y1, y2) :
        for y in range(x1, x2) :
            graph[x][y] = 1

#북동남서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
area = 1 
cnt = 0

def dfs(x, y) :
    global area
    graph[x][y] = 1
    for i in range(4) : 
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 0:
            area += 1
            dfs(nx, ny)

ans = []
for i in range(m) :
    for j in range(n) :
        if graph[i][j] == 0 :
            cnt += 1
            dfs(i, j)
            ans.append(area)
            area = 1

ans.sort()
print(len(ans))
print(*ans)