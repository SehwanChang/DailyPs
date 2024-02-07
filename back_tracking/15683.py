import sys
input = sys.stdin.readline
from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]


#남 동 북 서 
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

direction = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
}

cctv = deque()
for i in range(n) :
    for j in range(m) :
        if graph[i][j] != 6 and graph[i][j] != 0 : 
            cctv.append((i, j, graph[i][j]))

def move(x, y, direction, graph) :
    for d in direction :
        nx, ny = x, y
        while True :
            nx += dx[d]
            ny += dy[d]

            #범위 밖 or 벽 
            if (nx < 0 or nx >= n or ny < 0 or ny >= m) or graph[nx][ny] ==  6 : 
                break
            #cctv 영역이 아님 
            elif graph[nx][ny] != 0 :
                continue
            graph[nx][ny] = '#'

# 각 cctv마다 회전하면서 전부 #으로 바꿈 , 그떄마다 영역 카운트 , 최소면 업데이트 

def dfs(level, graph) :
    global min_area
    
    if level == len(cctv) :
        cnt = 0
        for i in range(n) :
            cnt += graph[i].count(0)
        min_area = min(cnt, min_area)
        return

    graph_copy = [[j for j in graph[i]] for i in range(n)] 
    x, y, number = cctv[level]
    for d in direction[number] : 
        move(x, y, d, graph_copy)
        dfs(level + 1, graph_copy)
        #이걸 안하면 이미 dfs 가 끝난 그래프를 시작으로 해서 탐색을 다시함. 제일중요!
        graph_copy = [[j for j in graph[i]] for i in range(n)]

min_area = 100000
dfs(0, graph)
print(min_area)