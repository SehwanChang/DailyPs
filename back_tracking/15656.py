import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
answer = []
def backtracking(level, idx) :
    if level == m:
        print(*answer)
        return
    for i in range(idx, n) :
        answer.append(nums[i])
        backtracking(level + 1 , idx)
        answer.pop()
backtracking(0, 0)