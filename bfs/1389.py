import sys
input = sys.stdin.readline
from collections import deque
n, m = map(int,input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m) :
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


answer = []
cnt = 0
for start in range(1, n + 1) :
    visited = [False] * (n + 1) 
    distance = [0] * (n + 1)
    q = deque([(start, 0)])
    visited[start] = True
    while q : 
        v, dist = q.popleft()
        for neighbor in graph[v] :
            if not visited[neighbor] :
                visited[neighbor] = True
                q.append((neighbor, dist + 1))
                distance[neighbor] = dist + 1
    answer.append(sum(distance))
print(*answer)
print(answer.index(min(answer)) + 1)

#1 -3 ,4 : 2 + 1 + 1 + 2 = 6
#2 - 3 : 2 + 1 + 2 + 3 = 8
#3- 1, 2, 4 : 1 + 1+ 1+ 2 = 5
#4 - 1, 3, 5 : 1+ 2 + 1+ 1 = 5
#5 - 4 : 2 + 3 + 2 + 1 = 8