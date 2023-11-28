import sys
input = sys.stdin.readline
r , c = map(int,input().split())
arr = [list(input().strip()) for i in range(r)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
alpha = set(arr[0][0])
ans = 0

def dfs(x, y, cnt) :
    global ans
    ans = max(ans, cnt)
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c :
            if  arr[nx][ny] not in alpha : 
                alpha.add(arr[nx][ny])
                dfs(nx, ny, cnt + 1)
                alpha.remove(arr[nx][ny])

dfs(0, 0, 1)
print(ans)
    
    