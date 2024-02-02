
#dp[i][j] : 숫자 i를  숫자j 개 사용해서 만들 수 있는 가짓수 
#숫자 여러개 중복 사용 가능 , 순서 다르면 다른 경우 

import sys
input = sys.stdin.readline
n, k = map(int, input().split())
dp = [[0] * (k + 1) for _ in range(n + 1)]
for i in range(n + 1) :
    for j in range(k + 1) :
        #숫자 j개를 이용해서 0 만드는 경우의 수 = 1 : 이게 핵심!!
        dp[0][j] = 1
for i in range(1, n + 1) :
    for j in range(1, k + 1) :
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
print(dp[n][k] % 1000000000)