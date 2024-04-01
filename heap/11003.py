import sys, heapq
from collections import deque
input = sys.stdin.readline
n, l = map(int, input().split())
nums = list(map(int, input().split()))
q = deque()
for i in range(n) :
    while q and (q[-1][1] > nums[i]) :
        q.pop()
    q.append((i + 1, nums[i]))
    if q[-1][0] - q[0][0] >= l :
        q.popleft()
    print(q[0][1], end = ' ')
# 입력 
# 12 3
# 1 5 2 3 6 2 3 7 3 5 2 6

# 출력
# 1 1 1 2 2 2 2 2 3 3 2 2
