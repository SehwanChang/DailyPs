t = int(input())
for i in range(1, t + 1) : 
    n = int(input())
    num = list(map(int, input().split()))
    dp = [0] * len(num)
    dp[0] = num[0]
    ans = -float("inf")
    for j in range(1, len(num))  :
        dp[j] = max(num[j], dp[j - 1] + num[j])
        ans = max(dp[j], ans)
    print("#{} {}".format(i, ans))