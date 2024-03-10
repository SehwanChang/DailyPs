import sys
input = sys.stdin.readline
from collections import deque
m, n = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(m)]
#dx : 오른쪽 1 , 왼쪽 -1 
#dy : 아래 1 ,위 -1 
dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

cnt = 0
for i in range(m) :
    for j in range(n) :
        if graph[i][j] == 1 :
            q = deque()
            q.append((i, j))
            graph[i][j] = 0
            while q :
                x, y = q.popleft()
                for k in range(8) :
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 1 :
                        q.append((nx, ny))
                        graph[nx][ny] = 0
            cnt += 1
print(cnt)