import sys 
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
visited = [False] * n
max_ans = -1000000000
arr = []

def backtracking(level) :
    global max_ans
    if level == n :
        ans = 0
        for i in range(n - 1) :
            ans += abs(nums[arr[i]] - nums[arr[i + 1]])
        max_ans = max(ans, max_ans)
    for i in range(n) :
        if not visited[i] :
            visited[i] = True
            arr.append(i)
            backtracking(level + 1)
            visited[i] = False
            arr.pop()
backtracking(0)
print(max_ans)
