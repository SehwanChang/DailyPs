import sys
input = sys.stdin.readline
from itertools import combinations
from collections import deque
n, m = map(int, input().split())
graph = [list(map(str,input().strip())) for _ in range(n)]
case = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y) :
    visited = [[-1] * m for _ in range(n)]
    q = deque()
    q.append((x, y))
    visited[x][y] = 0
    dist = 0
    while q :
        x, y = q.popleft()
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 'L' :
                if visited[nx][ny] == -1 :
                    visited[nx][ny] = visited[x][y] + 1
                    dist = max(dist, visited[nx][ny])
                    q.append((nx, ny))
    return dist

max_dist = 0
for i in range(n) :
    for j in range(m) :
        if graph[i][j] == 'L' :
            max_dist = max(max_dist, bfs(i, j))
print(max_dist)

#탐색 하면서 최솟값 -> 최댓값 갱신하는 순서로
# L : 육지, W : 바다, 육지만 이동 가능.
# 1칸 : 1시간
# 보물 2개: 가장 멀리있는곳.
# l, w : 전부 50 이하 