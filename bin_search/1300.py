n = int(input())
k = int(input())

start , end = 1, k
result = 0
while start <= end :
    mid = (start + end) // 2
    cnt = 0
    for i in range(1, n + 1) :
        cnt += min(mid // i , n)
    if cnt < k :
        start = mid + 1
    else : 
        result = mid
        end = mid - 1
print(result)