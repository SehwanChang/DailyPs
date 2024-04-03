import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
case = [(j, i) for i in range(m) for j in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
ans = 0

def bfs(i, j) :
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    cnt = 1
    flag = True
    while q :
        x, y = q.popleft()
        for k in range(4) :
            nx = x + dx[k]
            ny = y + dy[k] 
            if 0 <= nx < n and 0 <= ny < m :
                if not visited[nx][ny] :
                    if graph[nx][ny] == 2 :
                        cnt += 1
                        visited[nx][ny] = True
                        q.append((nx, ny))
                    elif graph[nx][ny] == 0 :
                        flag = False
    return cnt if flag else 0

for comb in combinations(case, 2) :
    case_1, case_2 = comb[0], comb[1]
    x1, y1 = case_1[0], case_1[1]
    x2, y2 = case_2[0], case_2[1]
    if graph[x1][y1] == 0 and graph[x2][y2] == 0 :
        visited = [[False] * m for _ in range(n)]
        graph[x1][y1], graph[x2][y2] = 1, 1
        tmp_ans = 0
        for i in range(n) :
            for j in range(m) :
                if graph[i][j] == 2 and not visited[i][j]:
                        tmp_ans += bfs(i, j)
        ans = max(ans, tmp_ans)
        #다 끝나면 돌 원위치  
        graph[x1][y1], graph[x2][y2] = 0, 0
print(ans)
# 1 : 나의 돌, 2 : 상대의 돌 , 최대 2개까지 