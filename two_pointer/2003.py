import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nums = list(map(int, input().split()))
start , end = 0, 1
cnt = 0

while end <= n and start <= end :
    tmp = sum(nums[start:end])
    if tmp == m :
        cnt += 1
        end += 1
    elif tmp < m :
        end += 1
    else :
        start += 1
print(cnt)
