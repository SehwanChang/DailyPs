import sys
input = sys.stdin.readline
n = int(input())
dp = [0] * (n + 1)
costs = []  
for i in range(n) :
    t, p = map(int,input().split())
    costs.append((t, p))
for i in range(n - 1, -1, -1) :
    if costs[i][0] + i > n :
        dp[i] = dp[i + 1]
    else : 
        dp[i] = max(dp[i + 1],dp[costs[i][0] + i] + costs[i][1])
print(dp[0])