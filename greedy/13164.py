import sys
input = sys.stdin.readline
n, k = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
gaps = []
for i in range(n - 1) :
    gaps.append(nums[i + 1] - nums[i])
gaps.sort()
print(sum(gaps[:n - k]))