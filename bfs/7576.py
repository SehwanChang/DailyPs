import sys
from collections import deque
input = sys.stdin.readline
m, n= map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

q = deque()
for i in range(n) :
    for j in range(m) :
        if graph[i][j] == 1 :
            q.append((i, j, 0))

while q :
    print('q : ', q)
    x, y, time = q.popleft()
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] :
            
            if graph[nx][ny] == 0 : 
                visited[nx][ny] = True
                graph[nx][ny] = 1
                q.append((nx, ny, time + 1))
for row in graph :
    if 0 in row :
        print(-1)
        exit()
print(time)
#1 : 익은 토마토, 0 : 익지 않은 토마토, -1 : 토마토가 들어있지 않은 칸 
# 여러분은 토마토가 모두 익을 때까지의 최소 날짜를 출력해야 한다. 
# 만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 
# 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.
