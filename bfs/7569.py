import sys
from collections import deque
input = sys.stdin.readline
m, n, h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
q = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                q.append((i, j, k, 0))
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
while q :
    z, x, y, time = q.popleft()
    for i in range(6) :
        nz = z + dz[i]
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m :
            if graph[nz][nx][ny] == 0 :
                graph[nz][nx][ny] = 1
                q.append((nz, nx, ny, time + 1))

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0: 
                print(-1)
                exit()
print(time)