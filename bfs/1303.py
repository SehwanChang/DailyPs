import sys
input = sys.stdin.readline
from collections import deque
m, n = map(int, input().split())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
white, blue = 0, 0
graph = [list(input().strip()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
def bfs(x, y) :
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    cnt = 1
    while q :
        x, y = q.popleft()
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] :
                if graph[nx][ny] == graph[x][y] :
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    cnt += 1
    return cnt 

for i in range(n) :
    for j in range(m) :
        if not visited[i][j] :
            res = bfs(i, j)
            if graph[i][j] == 'W' :
                white += res ** 2
            else :
                blue += res ** 2
print(white, blue)