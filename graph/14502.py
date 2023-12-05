from collections import deque
import sys
import copy
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

#바이러스 퍼트리기 
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def bfs():
    q = deque()
    tmp_graph = copy.deepcopy(graph)
    for i in range(n) :
        for j in range(m) : 
            if tmp_graph[i][j] == 2 :
                q.append((i, j))
    while q :
        x, y = q.popleft()
        for i in range(4) : 
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m :
                if tmp_graph[nx][ny] == 0 :
                    tmp_graph[nx][ny] = 2
                    q.append((nx, ny))
        global total_area
        cnt = 0
    for i in range(n) :
        cnt += tmp_graph[i].count(0)
    total_area = max(total_area, cnt)
def makewall(cnt) :
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m) :
            if graph[i][j] == 0 : 
                graph[i][j] = 1
                makewall(cnt + 1)
                graph[i][j] = 0

total_area = 0
makewall(0)
print(total_area)