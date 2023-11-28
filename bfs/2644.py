from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
a, b = map(int,input().split())
graph = [[] for _ in range(n + 1)]
m = int(input())
for i in range(m) :
    parent, child = map(int,input().split())
    graph[parent].append(child)
    graph[child].append(parent)

visited = [False] * (n + 1)
cnt = -1
q = deque([(a, 0)])
visited[a] = True
while q :
    current, cnt = q.popleft()
    if current == b :
        print(cnt)
        break
    for relative in graph[current] : 
        if not visited[relative] :
            visited[relative] = True
            q.append((relative, cnt + 1))
else :
    print(-1)