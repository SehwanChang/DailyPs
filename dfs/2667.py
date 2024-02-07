n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
#북 동 남 서
dx = [1 ,0, -1, 0]
dy = [0, 1, 0, -1]

cnt = 0
result = []

def dfs(x, y) :
    global cnt
    if 0 <= x < n and 0 <= y < n :
        if graph[x][y] == 1 :
            cnt += 1
            graph[x][y] = 0
            for i in range(4) :
                nx = x + dx[i] 
                ny = y + dy[i]
                dfs(nx, ny) 
         
for i in range(n) :
    for j in range(n) :
        if graph[i][j] == 1 :
            dfs(i, j)
            result.append(cnt)
            cnt = 0
result.sort()
print(len(result))
for i in result :
    print(i)