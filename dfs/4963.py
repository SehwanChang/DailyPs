import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
def dfs(x , y) :
    visited[x][y] = True
    for i in range(8) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1 and not visited[nx][ny]:
                dfs(nx,ny)
while True :
    w, h = map(int,input().split())
    if w == 0 and h == 0 :
        break
    graph = [[0] * w for i in range(h)]
    visited = [[False] * w for i in range(h)]
    #북 동 남 서 + 대각선
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    cnt = 0
    for i in range(h) :
       data = list(map(int,input().split()))
       graph[i]= data
    for i in range(h) :
        for j in range(w) :
            if visited[i][j] == False and graph[i][j] == 1 :
                dfs(i, j)
                cnt += 1
    print(cnt)