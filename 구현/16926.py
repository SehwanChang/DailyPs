import sys 
input = sys.stdin.readline
n, m, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)] 
for _ in range(r) :
    for i in range(min(n, m) // 2) :
        x, y = i, i
        tmp = graph[x][y]
        #좌
        for j in range(i + 1, n - i) :
            x = j
            prev = graph[x][y]
            graph[x][y] = tmp
            tmp = prev
        #하 
        for j in range(i + 1, m - i) :
            y = j
            prev = graph[x][y]
            graph[x][y] = tmp
            tmp = prev
        #우
        for j in range(i + 1, n - i) :
            x = n - j - 1
            prev = graph[x][y]
            graph[x][y] = tmp
            tmp = prev
        #상
        for j in range(i + 1, m - i) :
            y = m - j - 1
            prev = graph[x][y]
            graph[x][y] = tmp
            tmp = prev
for i in range(n) :
    for j in range(m) :
        print(graph[i][j], end= ' ')
    print()