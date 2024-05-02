from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
water = 0


def bfs(x, y):
    global water
    q = deque()
    q.append((x, y))
    visited = [[False] * m for _ in range(n)]
    height = graph[x][y]
    min_height = 10
    mini_pool = [(x, y)]
    visited[x][y] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if height >= graph[nx][ny] and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    mini_pool.append((nx, ny))

                elif height < graph[nx][ny]:
                    min_height = min(min_height, graph[nx][ny])
            else:
                return 0
    for pos in mini_pool:
        x, y = pos
        water += (min_height - graph[x][y])
        graph[x][y] = min_height


for i in range(1, n - 1):
    for j in range(1, m - 1):
        bfs(i, j)

print(water)
