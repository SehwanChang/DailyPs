import sys
input = sys.stdin.readline
from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
q = deque()
def bfs(i, j) :
    q.append((i, j, 0))
    visited[i][j] = True
    while q :
        x, y, dist = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] :
                if graph[nx][ny] == 1 :
                    visited[nx][ny] = True
                    graph[nx][ny] = dist + 1
                    q.append((nx, ny, dist + 1))
flag = 1
for i in range(n) :
    for j in range(m) :
        if graph[i][j] == 2 and flag == 1:
            flag = 0
            graph[i][j] = 0
            bfs(i, j)


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == False:  
            graph[i][j] = -1
for row in graph :
    print(' '.join(map(str, row)))