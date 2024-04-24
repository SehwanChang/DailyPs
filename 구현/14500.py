import sys
input = sys.stdin.readline
n, m = map(int, input().split())
blokcs = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
#현재까지 발견된 최대점수
max_sum = 0
def dfs(x, y, tmp, area) :
    global max_sum
    # 현재까지 발견된 최대점수 > 현재 경로에서 이론적으로 얻을 수 있는 최대점수 : 게산 종료
    if max_sum  >= max_value * (4 - area) + tmp :
        return
    if area == 4 :
        max_sum = tmp
        return 
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False :
            visited[nx][ny] = True
            #자기자신 : dfs 원리 생각해보기
            if area == 2 :
                dfs(x, y, tmp + blokcs[nx][ny] , area + 1)
                visited[nx][ny] = False
            dfs(nx, ny, tmp + blokcs[nx][ny] , area + 1)
            visited[nx][ny] = False

max_value = max(map(max, blokcs))
for i in range(n) :
    for j in range(m) :
        visited[i][j] = True
        dfs(i, j, blokcs[i][j], 1)
        visited[i][j] = False
print(max_sum)