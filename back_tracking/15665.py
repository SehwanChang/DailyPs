import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
ans = []
ans_set = set()
def backtracking(idx) :
    if len(ans) == m:
        ans_tuple = tuple(ans)
        if ans_tuple not in ans_set :
            print(*ans)
            ans_set.add(ans_tuple)
        return
    for i in range(idx, n) :
        ans.append(nums[i])
        backtracking(idx)
        ans.pop()
backtracking(0)