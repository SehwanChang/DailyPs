import sys
input = sys.stdin.readline
t = int(input())
for i in range(t) :
    n = int(input())
    price = []
    dp = [[0] * 3 for _ in range(n)]
    for _ in range(2) :
        price.append(list(map(int,input().split())))
    dp[0][1] = price[0][0]
    dp[0][2] = price[1][0]
    if n > 1 :
        print((max(price[0][0],price[1][0])))
        continue

    for j in range(n) :
        dp[j][0] = max(dp[j - 1][0], dp[j-1][1], dp[j - 1][2])
        dp[j][1] = max(dp[j - 1][0], dp[j - 1][2]) + price[0][j]
        dp[j][2] = max(dp[j - 1][0], dp[j -1][1]) + price[1][j]
    print(max(max(dp)))
#경우의 수 = 3가지 
# 1) 아무것도 선택하지 않음 : dp[i][0] 
# 2) 위에거 선택했을때 최댓값 : dp[i][1]
# 3) 아래거 선택했을때 최댓값 : dp[i]2]


#2
#30
#60


# 3
# 40 10 30
# 20 60 80
# 120



# 2
# 5
# 50 10 100 20 40
# 30 50 70 10 60
# 7
# 10 30 10 50 100 20 40
# 20 40 30 50 60 20 80