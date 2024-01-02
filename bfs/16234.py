import sys
from collections import deque
n, l, r = map(int, input().split())
graphs = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

q = deque()
def bfs(i, j) :
    unions = [(i, j)]
    q.append((i, j))
    visited[i][j] = 1
    while q :
        x, y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 :
                if l <= abs(graphs[x][y] - graphs[nx][ny]) <= r :
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    unions.append((nx, ny))
    return unions

day = 0
while True :
    move = False
    visited = [[0] * n for _ in range(n)]
    for i in range(n) :
        for j in range(n) :
            if visited[i][j] == 0 :
                country = bfs(i, j)
                if len(country) > 1:
                    move = True
                    total_pop = 0
                    for x, y in country :
                        total_pop += graphs[x][y]
                    country_count = len(country)
                    average_pop = total_pop // country_count
    
                    for x, y in country :
                        graphs[x][y] = average_pop
    if not move :
        print(day)
        break
    day += 1