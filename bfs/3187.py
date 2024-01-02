import sys
from collections import deque
input = sys.stdin.readline
n, m  = map(int, input().split())
graphs = [list(input().strip()) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

q = deque()
def bfs(i, j) :
    sheep, wolf = 0, 0
    q.append((i, j))
    if graphs[i][j] == 'v' :
        wolf += 1
    elif graphs[i][j] == 'k' :
        sheep += 1
    graphs[i][j] = '#'
    while q :
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graphs[nx][ny] != '#' :
                if graphs[nx][ny] == 'v' : 
                    wolf += 1
                elif graphs[nx][ny] == 'k' :  
                    sheep += 1
                graphs[nx][ny] = '#'
                q.append((nx, ny))
    return (sheep, 0) if sheep > wolf else (0, wolf)


answer = [0,0]
for i in range(n) :
    for j in range(m):
        if graphs[i][j] == 'v' or graphs[i][j] == 'k' :
            sheep, wolf = bfs(i, j)
            answer[0] += sheep
            answer[1] += wolf
print(*answer)
