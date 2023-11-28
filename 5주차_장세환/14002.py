import sys
input = sys.stdin.readline
n = int(input())
num = list(map(int,input().split()))
dp = [0] * n
dp[0] = 1
res = []
checked = [-1] * n
for i in range(n) :
    max_len = 0
    for j in range(i) :
        if num[i] > num[j] :
            if max_len < dp[j] :
                max_len = max(max_len, dp[j])
                checked[i] = j
    dp[i] = max_len + 1
idx = dp.index(max(dp))
while idx != -1 :
    res.append(num[idx])
    idx = checked[idx]
res = res[::-1]
print(max(dp))
print(*res)