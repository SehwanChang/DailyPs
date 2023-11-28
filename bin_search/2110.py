import sys
input = sys.stdin.readline
n , c = map(int,input().split())
arr = [int(input()) for i in range(n)]
arr.sort()
start , end = 1 , arr[-1] - arr[0]
result = 0
while start <= end :
    mid = (start + end ) // 2
    cnt = 1
    cur = arr[0]
    for i in range(1, n) :
        if arr[i] - cur >= mid :
            cnt += 1
            cur = arr[i]
    if cnt >= c : 
        start = mid + 1
        result = mid
    else :
        end = mid - 1
print(end)

