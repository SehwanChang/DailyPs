import sys
input = sys.stdin.readline
A = int(input())
a = list(map(int,input().split()))
dp = [0] * (A)
dp[0] = 1
for i in range(1, A): 
    max_len = 0
    for j in range(i) :
        if a[i] > a[j] :
            max_len = max(max_len, dp[j])
    dp[i] = max_len + 1
print(max(dp))