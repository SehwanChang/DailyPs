k , n = map(int, input().split())
arr = []
for i in range(k) :
    arr.append(int(input()))
start, end = 1, max(arr)
while start <= end : 
    mid = (start + end) // 2
    cnt = 0
    for cm in arr :
        cnt += cm // mid
    if cnt >= n :
        start = mid + 1
    else : 
        end = mid - 1
print(end)