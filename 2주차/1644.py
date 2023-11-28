import math

n = int(input())
prime_idx = [1 for i in range(n + 1)]
prime_idx[0] = 0
prime_idx[1] = 0
for i in range(2, int(n **0.5) + 1) :
    if prime_idx[i] :
        for j in range(2 * i, n + 1, i) :
            prime_idx[j] = 0
cnt = 0
start = 0
end = 0
prime = []
prime = [idx for idx, val in enumerate(prime_idx) if val == 1] 
while end <= len(prime) :
    ans = sum(prime[start:end])
    if ans == n :
        cnt +=1
        end +=1
    elif ans < n :
        end +=1
    else :
        start += 1
print(cnt)

#누적합 배열을 따로 짜면 더 시간복잡도가 좋은걸까?