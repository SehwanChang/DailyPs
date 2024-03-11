import sys
input = sys.stdin.readline
from collections import deque
m, n = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(m)]
sys.setrecursionlimit(10 ** 9)
#dx : 오른쪽 1 , 왼쪽 -1 
#dy : 아래 1 ,위 -1 
dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def dfs(x, y) :
    graph[x][y] = 0
    for k in range(8) :
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 1 :
            dfs(nx, ny)


cnt = 0
for i in range(m) :
    for j in range(n) :
        if graph[i][j] == 1 :
            dfs(i, j)
            cnt += 1
print(cnt)