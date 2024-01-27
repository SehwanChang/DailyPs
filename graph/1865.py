import sys
input = sys.stdin.readline
inf = float('inf')
t = int(input())

def belman_ford(start) :
        distance = [10001] * (n + 1)
        distance[start] = 0
        for i in range(n) :
                for cur_node, next_node, cost in graph :
                    if distance[next_node] > distance[cur_node] + cost :
                        distance[next_node] = distance[cur_node] + cost 
                        if i == n - 1 :
                            return True
        return False

for _ in range(t) :
    n, m, w = map(int, input().split())
    graph = []

    for i in range(m) :
        s, e, t = map(int,input().split())
        graph.append((s, e, t))
        graph.append((e, s, t))

    for j in range(w) :
        s, e, t = map(int,input().split())
        graph.append((s, e, -t))

    cycle = belman_ford(1)
    if cycle : 
        print('YES')
    else : 
        print('NO')