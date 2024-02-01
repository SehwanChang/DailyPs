import sys
input = sys.stdin.readline
n, s = map(int, input().split())
nums = list(map(int, input().split()))

cnt = 0
def backtracking(total, idx) :
    global cnt
    if idx > 0 and total == s :
        cnt += 1
    for i in range(idx, n) :
        backtracking(total + nums[i], i + 1)

backtracking(0, 0)
print(cnt)
