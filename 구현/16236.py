import sys
input = sys.stdin.readline
from collections import deque
n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]
total_fish = sum(sum(row) for row in area) - 9
visited = [[False] * n for _ in range(n)]

shark = 2
time = 0
if total_fish == 0 : 
    print(0)
    sys.exit()

if total_fish + 2 == shark :
    print(time)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
cur_x, cur_y = 0, 0
q = deque()
for i in range(n) :
    for j in range(n) :
        if area[i][j] == 9 :
            cur_x , cur_y = i, j
            q.append([(i, j)])


def bfs(): 
    dist = [[-1] * n for _ in range(n)]
    while q :
        x, y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False :
                #상어가 먹을 수 있는 생선
                if shark > area[nx][ny] and area[nx][ny] != 0 :
                    visited[nx][ny] = True
                    q.append([(nx, ny)])
                    shark += area[nx][ny]
                #상어가 먹을 수 없는 생선
                else : 
                    continue
    

print(total_fish)