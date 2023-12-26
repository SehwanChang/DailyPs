import sys
input = sys.stdin.readline
n, k = map(int, input().split())
kit = list(map(int, input().split()))

ans = 0
visited = [False] * n
def recur(x, level) :
    global ans
    if x < 500 :
        return
    if level == n :
        ans += 1
        return
    x -= k
    for i in range(n) :
        if not visited[i] :
            visited[i] = True
            recur(x + kit[i], level + 1)
            visited[i] = False
recur(500 , 0)
print(ans)