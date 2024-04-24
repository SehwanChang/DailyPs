import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
tmp = min(n, m) - 1
def isSquare(x, y, tmp) :
    if graph[x][y] == graph[x + tmp][y] == graph[x][y + tmp] == graph[x + tmp][y + tmp] :
        return True
    return False
while tmp >= 0 :
    for i in range(n) :
        for j in range(m) :
            if i + tmp < n and j + tmp < m :
                if isSquare(i, j, tmp) :
                    print((tmp + 1) ** 2)
                    sys.exit()
    tmp -= 1
print(1)