import sys
input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
result = 0

def dfs(x, y, condition):  # condition 1: 가로, 2: 대각선, 3: 세로
    global result
    if x == n - 1 and y == n - 1:
        result += 1
        return

    # 진행 방향이 가로
    if (condition == 1 or condition == 2) and y + 1 < n and graph[x][y + 1] == 0:
        dfs(x, y + 1, 1)

    # 진행 방향이 세로
    if (condition == 2 or condition == 3) and x + 1 < n and graph[x + 1][y] == 0:
        dfs(x + 1, y, 3)

    # 진행 방향이 대각선
    if x + 1 < n and y + 1 < n and graph[x + 1][y] == 0 and graph[x][y + 1] == 0 and graph[x + 1][y + 1] == 0:
        dfs(x + 1, y + 1, 2)

dfs(0, 1, 1)
print(result)
