import sys
input = sys.stdin.readline
from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def bfs(x, y) :
    tmp = graph[x][y]
    if graph[x][y] == 0 or visited[x][y] :
        return 0
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    flag = True # 봉우리 여부 체크
    while q :
        cx, cy = q.popleft()
        for dx, dy in directions :
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < m :
                if not visited[nx][ny] and graph[nx][ny] == tmp :
                    visited[nx][ny] = True
                    q.append((nx, ny))
                elif graph[nx][ny] > tmp :
                    flag = False
    return flag

ans = 0
for i in range(n) :
    for j in range(m) :
        if not visited[i][j] and bfs(i, j) :
                ans += 1
print(ans)