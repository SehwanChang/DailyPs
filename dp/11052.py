import sys
input = sys.stdin.readline
n = int(input())
price = [0] + list(map(int,input().split()))
# dp[i] : i 개를 구매했을때 최대 수익   
# dp[i] = max(1<= j <= i (price[j] + dp[i - j]))
dp = [0] * (n + 1)
for i in range(1, n + 1) :
    for j in range(1, i + 1) :
        dp[i] = max(dp[i], price[j] + dp[i - j])
print(max(dp))


# 4
# 1 5 6 7
# 10

# 5
# 10 9 8 7 6
# 50

# 10
# 1 1 2 3 5 8 13 21 34 55
# 55