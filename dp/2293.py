import sys
input = sys.stdin.readline
n, k = map(int, input().split())
coins = [int(input()) for i in range(n)]

# dp[i] : i원을 만들 수 있는 경우의 수  
dp = [0] * (k + 1)
dp[0] = 1

for coin in coins :
    for i in range(coin, k + 1) :
        dp[i] += dp[i - coin]
print(dp[k])

#동전을 사용해서 (개수 제한 x) k원을 만들 수 있는 경우의 수 

# 3 10
# 1
# 2
# 5

# 10