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
            next = x + d
            if (0 <= next < n) and not visited[next]:
                q.append(next)
                visited[next] = True
print(visited.count(1))