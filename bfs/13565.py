import sys
input = sys.stdin.readline
from collections import deque
m, n = map(int,input().split())
graph = [list(map(int, input().strip())) for _ in range(m)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
q = deque()
for i in range(m) :
    for j in range(n) :
        if graph[i][j] == 1 :
            q.append((i, j))
while q :
    x, y = q.popleft()
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 1:
            q.append((nx, ny))
            graph[nx][ny] = 2
print(graph)
if 2 in graph[m - 1] :
    print('YES')
else :
    print('NO')