import sys
input = sys.stdin.readline
from collections import deque
t = int(input())
graph = [deque(map(int,input().strip())) for _ in range(t)]
k = int(input())
orders = [list(map(int, input().split())) for _ in range(k)]

def rotate(s, direction) :
    s.rotate(1 if direction == 1 else -1)
    return s

for order in orders : 
    num, direction = order[0] - 1, order[1]
    rotate_direction = [0] * t
    rotate_direction[num] = direction

    for i in range(num , t - 1) : 
        if graph[i][2] != graph[i + 1][6] :
            rotate_direction[i + 1] = -rotate_direction[i]
    for i in range(num, 0 , -1) :
        if graph[i][6] != graph[i - 1][2] :
            rotate_direction[i - 1] = -rotate_direction[i]
    for i in range(t) :
        if rotate_direction[i] != 0 : 
            graph[i] = rotate(graph[i], rotate_direction[i])
ans = 0
for i in range(t):
    ans += 1 if graph[i][0] == 1 else 0
    
print(ans)

#rotate에서 rotate(1)은 시계방향으로 회전함 [1,2,3,4] 면 [4,1,2,3]
#rotate(-1)은 [2, 3, 4, 1]
#deque 익혀두기