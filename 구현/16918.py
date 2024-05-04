from collections import deque
import sys
input = sys.stdin.readline
r, c, n = map(int, input().split())
graph = [list(map(str, input().strip())) for _ in range(r)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# n 초 지난 후 격자판 상태 출력.
time = 1
q = deque()

# 폭탄 폭발


def bomb(q, graph):
    while q:
        x, y = q.popleft()
        graph[x][y] = '.'
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] == 'O':
                graph[nx][ny] = '.'


def simulate(t):
    global q, graph
    # 1초: 처음 폭탄의 위치 전부 저장.
    if t == 1:
        for i in range(r):
            for j in range(c):
                if graph[i][j] == 'O':
                    q.append((i, j))
    elif t % 2 == 1:
        bomb(q, graph)
        for i in range(r):
            for j in range(c):
                if graph[i][j] == 'O':
                    q.append((i, j))
    # 2초에전부 폭탄으로 채워도 3초에는 (1초에 저장된 q의 폭탄이 터짐 )
    else:
        graph = [['O'] * c for _ in range(r)]


# n초가 지날떄마다
for i in range(1, n + 1):
    simulate(i)

for i in graph:
    print(''.join(i))
