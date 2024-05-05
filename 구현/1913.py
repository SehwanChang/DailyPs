import sys
input = sys.stdin.readline
n = int(input())
target = int(input())
graph = [[0] * n for _ in range(n)]

#  0:아래, 1:오른쪽, 2:위, 3:왼쪽
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
dir = 0

pos_x = pos_y = 0
num = n * n
ans = [0, 0]
while num > 1:
    if num == target:
        ans[0] = pos_x + 1
        ans[1] = pos_y + 1
    graph[pos_x][pos_y] = num
    nx, ny = pos_x + dx[dir], pos_y + dy[dir]
    if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
        pos_x, pos_y = nx, ny
        num -= 1
    else:
        dir = (dir + 1) % 4

graph[(n - 1) // 2][(n - 1) // 2] = 1
for row in graph:
    print(*row)

print(*ans)
