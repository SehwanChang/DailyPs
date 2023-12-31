import sys
from collections import deque
n, m, k = map(int,input().split())
graph = [[0] * m for _ in range(n)]
for i in range(k) :
    r, c = map(int, input().split())
    graph[r - 1][c - 1] = 1

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


ans = []
def bfs(a, b) :
    cnt = 1
    q = deque()
    graph[a][b] = 0
    q.append((a, b))
    while q :
        x, y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] :
                graph[nx][ny] = 0
                q.append((nx, ny))
                cnt += 1
    return cnt

for i in range(n) :
    for j in range(m) :
        if graph[i][j] == 1 :
            ans.append(bfs(i, j))
print(max(ans))
