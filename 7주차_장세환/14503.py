import sys
input = sys.stdin.readline
from collections import deque
n , m = map(int,input().split())
r, c, d = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

visited = [[0]*m for _ in range(n)]
visited[r][c] = 1

#북 동 남 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

cnt = 1

#flag = 1 : 청소 한 상태

while True:
    flag = 0            
    for i in range(4):  
        d = (d+3) % 4 
        nr = r + dr[d]
        nc = c + dc[d]

        if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == 0:
            if visited[nr][nc] == 0:
                visited[nr][nc] = 1
                cnt += 1
                r = nr
                c = nc
                flag = 1       
                break

    if flag == 0:              
        if arr[r-dr[d]][c-dc[d]] == 1:
            print(cnt)
            break
        else:
            r, c = r-dr[d], c-dc[d]