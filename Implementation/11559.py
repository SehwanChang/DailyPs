import sys
input = sys.stdin.readline
from collections import deque
graph = [list(map(str, input().strip())) for _ in range(12)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#bfs: 탐색 후 연결된것들 리스트 반환 
def bfs(x, y) :
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    connected = [(x, y)]
    while q :
        x, y = q.popleft()
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 12 and 0 <= ny < 6 and not visited[nx][ny] :
                if graph[x][y] == graph[nx][ny] :
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    connected.append((nx, ny))
    return connected
#def move : 이동하기 
def move() :
    for y in range(6) :
        for x in range(10, -1, -1) : #두번째 행부터 위로 순회
            for k in range(11, x, -1) : #현재 행 x에서 아래로 순회
                if graph[x][y] != '.' and graph[k][y] == '.' :
                    graph[k][y] = graph[x][y]
                    graph[x][y] = '.'

#def delete : 그래프 '.' 변환 
def delete(connected) :
    for x, y in connected :
        graph[x][y] = '.'
combo = 0
while True :
    visited = [[False] * 6 for _ in range(12)]
    flag = False
    for i in range(12) :
        for j in range(6) :
            if graph[i][j] != '.' and not visited[i][j] :
                connected = bfs(i, j)
                if len(connected) >= 4 :
                    delete(connected)
                    flag = True
    if flag :
        move()
        combo += 1
    else :
        break
print(combo)