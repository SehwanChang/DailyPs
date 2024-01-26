import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())
graph = [-1] * 100001
q = deque()
q.append(n)
graph[n] = 0

while q :
    cur = q.popleft()
    if cur == k : 
        print(graph[cur])
        break
    for next in (cur * 2, cur - 1, cur + 1) :
        if 0 <= next <= 100000 and graph[next] == -1 :
            if next == cur * 2 :
                graph[next] = graph[cur]
                
            else :
                graph[next] = graph[cur] + 1
            q.append(next)