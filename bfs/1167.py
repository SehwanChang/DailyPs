import sys
from collections import deque
input = sys.stdin.readline
v = int(input())
graph = [[] for _ in range(v + 1)]
for _ in range(v) :
    info = list(map(int, input().split()))
    for i in range(1, len(info) - 2, 2) :
        graph[info[0]].append((info[i], info[i + 1]))
def bfs(start) :
    visited = [-1] * (v + 1)
    q = deque()
    q.append(start)
    visited[start] = 0
    max_tree = [0, 0]
    
    while q :
        t = q.popleft()
        for e, w in graph[t] :
            if visited[e] == -1 :
                visited[e] = visited[t] + w
                q.append(e)
                if max_tree[0] < visited[e] :
                    max_tree = visited[e], e
    return max_tree
dist, node = bfs(1)
dist, node = bfs(node)
print(dist)