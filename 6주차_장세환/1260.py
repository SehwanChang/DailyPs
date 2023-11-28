# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 
# 정점 번호는 1번부터 N번까지이다.


# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 
# 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4

#  2 - - 4
#  |   / |
#  |  /  |
#  1 - - 3

# 1 2 4 3 : dfs
# 1 2 3 4 : bfs
import sys
input = sys.stdin.readline
from collections import deque

def dfs (graph, v, visited):
    visited[v] = True
    print(v, end = ' ')
    for i in graph[v] :
        if not visited[i] :
            dfs(graph, i, visited)

def bfs(graph, v, visited) :
    queue = deque([v])
    visited[v] = True
    
    while queue :
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v] :
            if not visited[i] :
                queue.append(i)
                visited[i] = True

n , m , v = map(int,input().split())
graph = [[] for i in range(n + 1)]
visited_dfs = [False] * (n + 1)
visited_bfs = [False] * (n + 1)
for i in range(m) :
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(n + 1) :
    graph[i].sort()

dfs(graph, v, visited_dfs)
print()
bfs(graph, v, visited_bfs)
