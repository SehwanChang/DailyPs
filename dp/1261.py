import sys
input = sys.stdin.readline
from collections import deque
m, n = map(int, input().split())
graph = [list(map(int,input().strip())) for _ in range(n)]
dist = [[-1] * m for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y) :
    q = deque()
    q.append((x, y))
    dist[0][0] = 0
    while q:
        x, y = q.popleft()
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m :
			          #아직 방문하지 않은 경우 
                if dist[nx][ny] == -1 :
                    if graph[nx][ny] == 0 :
                        dist[nx][ny] = dist[x][y]
                        #가중치가 0 : 먼저 더해야함 (append left)
                        q.appendleft((nx, ny))
                    else :
                        dist[nx][ny] = dist[x][y] + 1
                        #가중치가 1 : 나중에 더해야함
                        q.append((nx, ny))
            

bfs(0, 0)
print(dist[n - 1][m - 1])