import sys
input = sys.stdin.readline
n, m = map(int, input().split())
parent = list(range(n + 1))
def find(x) :
    if parent[x] == x :
        return x
    else : 
        parent[x] = find(parent[x])
        return parent[x]
def union(x, y) :
    x = find(x)
    y = find(y)

    if x != y :
        parent[y] = x

for i in range(m) :
    u , v = map(int,input().split())
    union(u, v)

for i in range(1, n + 1) :
    find(i)

answer = len(set(parent[1:]))
print(answer)
