import sys
input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0] * n for _ in range(n)] for _ in range(3)]
dp[0][0][1] = 1
# 0 : 가로, 1 : 세로, 2 : 대각선

for i in range(2,n):
    if graph[0][i] == 0:
        dp[0][0][i] = dp[0][0][i - 1]

for x in range(1, n) :
    for y in range(1, n) :
        #현재 위치 대각 :
        if graph[x][y - 1] == 0 and graph[x - 1][y] == 0 and graph[x][y] == 0 :
            dp[2][x][y] = dp[0][x - 1][y - 1] + dp[1][x - 1][y - 1] + dp[2][x - 1][y - 1]
        if graph[x][y] == 0:
            #현재 위치 가로 
            dp[0][x][y] = dp[0][x][y -1] + dp[2][x][y - 1]
            #현재 위치 세로 
            dp[1][x][y] = dp[1][x -1][y] + dp[2][x - 1][y]
print(sum(dp[i][n -1][n - 1] for i in range(3)))