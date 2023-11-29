import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int,input().split())) for i in range(n)]
#dp[i][j] : (1,1) ~ (i, j) 까지의 누적합
dp = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1) :
    for j in range(1, n + 1) :
        #중복된 부분은 마지막에 뺴줘야함.
        dp[i][j] = arr[i - 1][j - 1] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]
for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    ans = dp[x2][y2] - dp[x2][y1 -1] - dp[x1 -1][y2] + dp[x1 - 1][y1 - 1]
    print(ans)

