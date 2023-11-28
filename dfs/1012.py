import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
def dfs(x,y) :
    global cnt
    if x < 0 or x >= n or y < 0 or y >= m :
        return
    if graph[x][y] == 1 :
        graph[x][y] = -1
        for i in range (4) :
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
t = int(input())
for i in range (t) :
    m , n , k = map(int,input().split())
    graph = [[0] * m for i in range(n)]

    cnt = 0
    #북 동 남 서
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for j in range (k) :
        M , N = map(int,input().split())
        graph[N][M] = 1
    for i in range(n) :
        for j in range(m) :
            if graph[i][j] == 1 :
                dfs(i, j)
                cnt += 1
    print(cnt)