import sys
from collections import deque

input = sys.stdin.readline
n , m = map(int, input().split())
queue = deque() # shark의 위치를 담는 list
shark = [[] for i in range(n)]
visited = [[False] * m for i in range(n)]
distance = [[0] * m for i in range(n)]

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]


def bfs() :
    while queue :
        x, y = queue.popleft()
        for i in range(8) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] :
                visited[nx][ny] = True
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx,ny))


for i in range(n) :
    shark[i] = list(map(int,input().split()))

for i in range(n) :
    for j in range(m) :
        if shark[i][j] == 1 :
            queue.append((i,j))
            visited[i][j] = True
bfs()
max_distance = max(map(max,distance))
print(max_distance)