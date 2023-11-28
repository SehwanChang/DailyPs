import sys
input = sys.stdin.readline
from collections import deque
n, m = map(int,input().split())
graph = [[] for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n) :
    graph[i]= list(map(int, input().strip()))

q = deque([(0, 0, 1)])
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
cnt = 0 

while q :
    x , y, dist = q.popleft()
    if x == n - 1 and y == m - 1 :
        print(dist)
        sys.exit()
    visited[x][y] = 1
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1 and visited[nx][ny] == 0 :
            visited[nx][ny] = 1
            q.append((nx, ny, dist + 1))
print(-1)

