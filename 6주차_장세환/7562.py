import sys
from collections import deque
input = sys.stdin.readline


n = int(input())
queue = deque()

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

def bfs():
    while queue:
        x , y = queue.popleft()
        for i in range (8) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny] :
                queue.append((nx,ny))
                visited[nx][ny] = True
                distance[nx][ny] = distance[x][y] + 1

for i in range(n) :
    l = int(input())
    src_x, src_y = map(int,input().split())
    dest_x, dest_y = map(int,input().split())
    queue.append((src_x,src_y))
    visited = [[False] * l for i in range(l)]
    distance = [[0] * l for i in range(l)]
    visited[src_x][src_y] = True
    bfs()
    print(distance[dest_x][dest_y])