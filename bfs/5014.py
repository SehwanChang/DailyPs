import sys 
input = sys.stdin.readline
from collections import deque
f, s, g, u, d = map(int, input().split())
stairs = deque()
stairs.append(s)
dist = [0] * (f + 1)

cnt = 0
while stairs :
    cur = stairs.popleft()
    if cur == g :
        print(dist[cur])
        break
    for next in (cur + u, cur - d) :
        if next == cur :
            continue
        if 1 <= next <= f and dist[next] == 0 :
            dist[next] = dist[cur] + 1
            stairs.append(next)
else :
    print('use the stairs')