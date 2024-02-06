import sys
input = sys.stdin.readline
from collections import deque
a, b, c = map(int, input().split())

q = deque()
visited = [[False] * (b + 1) for _ in range(a + 1)]
def move(x, y) :
    if not visited[x][y] :
        visited[x][y] = True
        q.append((x, y))

ans = []

q.append((0, 0))
visited[0][0] = True
while q : 
    x, y = q.popleft()
    z = c - x - y
    if x == 0 :
        ans.append(z)

    # 물 옮기는 경우 6가지 : x y / x z / y x / y z / z x / z y
    water = min(x, b - y)
    move(x - water, y + water)

    water = min(x, c - z)
    move(x - water, y)

    water = min(y, a - x)
    move(x + water, y - water)

    water = min(y, c - z)
    move(x, y - water)

    water = min(z, a - x)
    move(x + water, y)

    water = min(z, b - y)
    move(x, y + water)

ans.sort()
print(*ans)