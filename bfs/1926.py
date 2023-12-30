import sys
from collections import deque
n, m = map(int,input().split())
papers = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(a, b) :
    q = deque()
    cnt= 1
    papers[a][b] = 0
    q.append((a,b))
    while q :
        x, y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and papers[nx][ny] == 1 :
                papers[nx][ny] = 0
                cnt += 1
                q.append((nx, ny))
    return cnt
ans = []    
for i in range(n) :
    for j in range(m) :
        if papers[i][j] == 1 :
            ans.append(bfs(i, j))
if len(ans) == 0 :
    print('0')
    print('0')
else : 
    print(len(ans))
    print(max(ans))