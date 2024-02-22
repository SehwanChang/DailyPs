import sys
input = sys.stdin.readline
n = int(input())
stats = list(map(int, input().split()))
left, right = 0, n - 1
ans = 0

while left + 1 < right :
    ans = max(ans,(right - left - 1) * min(stats[left],stats[right]))
    if stats[left] < stats[right] :
        left += 1
    else :
        right -= 1
print(ans)