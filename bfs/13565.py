import sys
input = sys.stdin.readline
from collections import deque
m, n = map(int,input().split())
graph = [list(map(int, input().strip())) for _ in range(m)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
q = deque()
for i in range(n) :
    if graph[0][i] == 0 :
        q.append((0, i))

while q :
    x, y = q.popleft()
    graph[x][y] = 2
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 0:
            graph[nx][ny] = 2
            q.append((nx, ny))
print('YES') if 2 in graph[-1] else print('NO')
