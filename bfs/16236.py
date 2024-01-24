import sys
input = sys.stdin.readline
from collections import deque
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

x, y, size = 0, 0, 2
for i in range(n) :
    for j in range(n) :
        if graph[i][j] == 9 :
            x, y = i, j
            break

def bfs(x, y, shark_size) :
    distance = [[0] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    sub_fish = []
    while q :
        x, y, = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] :
                if graph[nx][ny] <= shark_size :
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    distance[nx][ny] = distance[x][y] + 1

                    if graph[nx][ny] < shark_size and graph[nx][ny] != 0 : #먹을 수 있는 후보들 
                        sub_fish.append((nx, ny, distance[nx][ny]))
    return sorted(sub_fish, key = lambda x: (-x[2], -x[0], -x[1]))

cnt, res = 0, 0
while True:
    shark = bfs(x, y, size)

    if len(shark) == 0 :
        break
    nx, ny, dist = shark.pop()
    res += dist

    graph[x][y], graph[nx][ny] = 0, 0
    x, y = nx, ny

    cnt += 1
    if cnt == size :
        size += 1
        cnt = 0
print(res)