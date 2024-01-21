n = int(input())
dp = [0, 1]
for i in range(2, n +1) :
   tmp = 1e9
   j = 1
   while (j ** 2) <= i :
      tmp = min(tmp, dp[i - (j ** 2)])
      j += 1
   dp.append(tmp + 1)
   
print(dp[n])    
