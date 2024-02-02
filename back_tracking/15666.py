import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
ans = []
ans_set = set()
def backtracking(idx) :
    if len(ans) == m:
        ans_sorted = sorted(ans)
        ans_tuple = tuple(ans_sorted)
        if ans_tuple not in ans_set :
            print(*ans)
            ans_set.add(ans_tuple)
        return
    for i in range(idx, n) :
        ans.append(nums[i])
        backtracking(i)
        ans.pop()
backtracking(0)

# 1 1 7 9
#1 1
#1 7
#1 9
#7 7
#7 9
#9 9