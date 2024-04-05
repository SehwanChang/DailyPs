import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
nums.sort()
cnt = 0
for i in range(n) :
    target = nums[i]
    left, right = 0, n - 1
    while left < right :
        #target = target + 0 으로 세는 경우 제외 
        if left == i :
            left += 1
            continue
        if right == i :
            right -= 1
            continue
        tmp = nums[left] + nums[right]
        if tmp == target : 
            cnt += 1
            break
        elif tmp < target : 
            left += 1
        else :
            right -= 1
print(cnt)