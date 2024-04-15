import sys
input = sys.stdin.readline
n = int(input())
nums = [i for i in range(1, n + 1)]
visited = [False] * n
tmp = []

def dfs(level) :
    if level == n :
        print(*tmp)
    for i in range(1, n + 1) :
        if i not in tmp :
            tmp.append(i)
            dfs(level + 1)
            tmp.pop()
dfs(0)