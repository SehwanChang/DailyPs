import sys
input = sys.stdin.readline
from collections import deque
n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
q = deque()

def bfs(i, j) :
    cnt = 0
    q.append((i, j))
    graph[i][j] = 1
    while q :
        x, y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 'P':
                    cnt += 1
                    graph[nx][ny] = 1
                    q.append((nx, ny))
                elif graph[nx][ny] != 'X' and graph[nx][ny] != 1  :
                    graph[nx][ny] = 1
                    q.append((nx, ny))
    return cnt

ans = 0
for i in range(n) :
    for j in range(m) :
        if graph[i][j] == 'I' :
            ans = bfs(i, j)
if ans == 0 :
    print('TT')
else : 
    print(ans)

# X = 벽, I = 도연, P = 사람 
# 아무도 못만남 : TT