from bisect import bisect_left, bisect_right
n , m = map(int,input().split())
trees = list(map(int,input().split()))
trees.sort()
start, end = 0, max(trees)
while start < end :
    mid = (start + end) // 2
    total = 0
    idx = bisect_right(trees, mid)
    total = sum([tree - mid for tree in trees if tree > mid])
        
    if total < m :
        end = mid - 1
    else :
        start = mid + 1
#10 15 17 20