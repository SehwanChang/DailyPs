import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
nums_set = set()
answer = []
def backtracking(level, idx) :
    if level == m :
        answer_tuple = tuple(answer)
        if answer_tuple not in nums_set :
            print(*answer)
            nums_set.add(answer_tuple)
        return
    for i in range(idx, n) :
        answer.append(nums[i])
        backtracking(level + 1 , i + 1)
        answer.pop()
backtracking(0, 0)