from collections import deque
import sys
input = sys.stdin.readline

dx = [1, 0]
dy = [0, 1]
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
q = deque()
q.append((0, 0))

while q:
    x, y = q.popleft()
    if graph[x][y] == 0:
        break
    elif graph[x][y] == -1:
        flag = True
        print("HaruHaru")
        sys.exit()
    for i in range(2):
        nx = x + dx[i] * graph[x][y]
        ny = y + dy[i] * graph[x][y]
        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True

print('Hing')


# 그래프이 숫자 : 한ㅓㄴ에 이동해야 하는 숫자
