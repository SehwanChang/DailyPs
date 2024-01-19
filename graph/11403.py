import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
def bfs(start) :
    q = deque()
    q.append(start)
    while q :
        a = q.popleft()
        for i in range(n) :
            if  graph[a][i] and not visited[start][i] :
                q.append(i)
                visited[start][i] = 1
for i in range(n) : 
    bfs(i)
for i in visited :
    print(*i)