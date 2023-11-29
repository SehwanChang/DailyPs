import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t) :
    n = int(input())
    dp = [list(map(int, input().split())) for _ in range(2)]
    if n > 1 :
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]
    for i in range(2, n) :
        # 위쪽 스티커 선택하는 경우 : 이전 열에서 아래쪽 or 아무것도 선택 x
        dp[0][i] += max(dp[1][i - 1], dp[1][i -2])
        # 아래쪽 스티커 선택하는 경우 : 이전열에서 위쪽 or 아무것도 선택 x
        dp[1][i] += max(dp[0][i - 1], dp[0][i - 2])
    print(max(dp[0][n-1],dp[1][n-1]))