n , k = map(int,input().split())
prime = [0 for i in range(n + 1)]
idx = []
for i in range (2, n + 1) :
    for j in range(i, n + 1 , i) :
        if prime[j] == 0 : 
            prime[j] = 1
            idx.append(j)
        if len(idx) >= k :
            break
print(idx[k - 1])   