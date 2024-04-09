import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
prefix = [0] *  n
prefix[0] = nums[0]
for i in range(1, n) :
    prefix[i] = prefix[i - 1] + nums[i]
m = int(input())
for _ in range(m) :
    start, end = map(int, input().split())
    ans = prefix[end - 1] - prefix[start - 1] + nums[start - 1]
    print(ans)
# 5
# 10 20 30 40 50    
# 10 30 60 100 150