import sys
from collections import deque
input = sys.stdin.readline
graph = [deque(map(int,input().strip())) for _ in range(4)]
k = int(input())
orders = [list(map(int, input().split())) for _ in range(k)]
ans = 0 
def rotate(s, direction) : 
    s.rotate(1 if direction == 1 else -1)
    return s
for order in orders :
    num, direction = order[0] - 1, order[1]
    rotate_direction = [0] * 4
    rotate_direction[num] = direction

    for i in range(num, 3) :
        if graph[i][2] != graph[i + 1][6] : 
            rotate_direction[i + 1] = -rotate_direction[i]
    for i in range(num, 0, -1) : 
        if graph[i][6] != graph[i -1][2] : 
            rotate_direction[i - 1] = -rotate_direction[i]
    
    for i in range(4) :
        if rotate_direction[i] != 0 :
            graph[i] = rotate(graph[i], rotate_direction[i])
for i in range(4) :
    ans += (2 ** i ) if graph[i][0] == 1 else 0
print(ans)

