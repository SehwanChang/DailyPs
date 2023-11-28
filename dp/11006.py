import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t) :
    n = int(input())
    dp = [[0] * n for _ in range (n)]
    sums = [0] * (n + 1)
    files = list(map(int,input().split()))
    for i in range(1, n + 1) :
        sums[i] = sums[i - 1] + files[i - 1]
    # l : 파일의 갯수 = 2개 ~ n개까지 합칠 수 있음
    for file in range(2, n + 1) :
        for start in range(n - file + 1) :
            end = start + file - 1
            dp[start][end] = float('inf')
            for tmp in range(start, end) :
                cost = sums[end + 1] - sums[start] # start ~ end까지의 구간합
                dp[start][end] = min(dp[start][end],dp[start][tmp] + dp[tmp + 1][end] + cost)

    print(dp[0][n - 1])