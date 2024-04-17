from collections import deque
n = int(input())
dist = list(map(int, input().split()))
q = deque()
s = int(input()) - 1
visited = [False] * n
q.append(s)
visited[s] = True
while q :
    x = q.popleft()
    for d in [-dist[x], dist[x]]:
            t = x + d
            if (0 <= t < n) and not visited[t]:
                q.append(t)
                visited[t] = 1
print(visited.count(1))