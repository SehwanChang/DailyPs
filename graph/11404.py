import sys
input = sys.stdin.readline
inf = float('inf')

n = int(input())
m = int(input())
dist = [[inf] * (n + 1) for _ in range(n + 1)]
for _ in range(m): 
    a, b, w = map(int, input().split())
    if dist[a][b] > w :
        dist[a][b] = w

def floyd() :    
    for i in range(1, n + 1): 
        dist[i][i] = 0
    for k in range(1, n + 1) :
        for i in range(1, n + 1) :
            for j in range(1, n + 1) :
                if dist[i][j] > dist[i][k] + dist[k][j] :
                    dist[i][j] = dist[i][k] + dist[k][j] 
    return dist

dist = floyd()
for i in range(1, n + 1) :
    for j in range(1, n + 1) :
        if dist[i][j] == inf :
            print(0, end = ' ')
            continue
        print(dist[i][j], end = ' ')
    print()