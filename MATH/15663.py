import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
combi = [] 
visited = [False] * n
def dfs() :
    if len(combi) == m :
        print(*combi)
        return
    tmp = 0
    for i in range(n) :
        if not visited[i] and tmp != nums[i] :
            visited[i] = True
            combi.append(nums[i])
            tmp = nums[i]
            dfs()
            visited[i] = False
            combi.pop()
dfs()