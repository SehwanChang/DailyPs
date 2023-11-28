import sys
input = sys.stdin.readline
from bisect import bisect_left
n = int(input())
items = list(map(int,input().split()))
LIS = [items[0]]
for item in items :
    if LIS[-1] < item :
        LIS.append(item)
    else :
        idx = bisect_left(LIS, item)
        LIS[idx] = item
print(len(LIS))