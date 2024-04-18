import sys
input = sys.stdin.readline
from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
dic = dict()
def bfs(x, y, cnt) :
    q = deque()
    visited[x][y] = cnt
    q.append((x, y))
    while q :
        x, y = q.popleft()
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m :
                if not visited[nx][ny] and graph[nx][ny] :
                    visited[nx][ny] = cnt
                    q.append((nx, ny))
cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] and not visited[i][j]:
            cnt += 1
            bfs(i,j,cnt)

for i in range(n):
    for j in range(m):
        if visited[i][j] > 0:
            if not visited[i][j] in dic:
                dic[visited[i][j]] = 1
            else:
                dic[visited[i][j]] += 1

ans = 0
for i in range(n) :
    for j in range(m) :
        if graph[i][j] == 0 :
            neighbor = []
            for k in range(4) :
                nx, ny = i + dx[k], i + dy[k]
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] :
                    neighbor.append((nx, ny))
                res = 0
                for tmp in (set(neighbor)) :
                    res += dic[tmp]
                ans = max(ans, res + 1)
print(ans)
