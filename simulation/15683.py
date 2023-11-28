# 6 6
# 1 0 0 3 3 3
# 3 1 0 3 3 3
# 3 3 1 3 3 3
# 3 3 3 1 3 3
# 3 3 3 0 1 3
# 3 3 3 0 0 1
# 1번 : 1방향 , 2번 : 2방향 (반대), 3번 : 2방향(직각)
#4번 : 3방향, 5번 : 4방향

import sys
import copy
input = sys.stdin.readline
n , m = map(int,input().split())
cctv = []
office = []

direction = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]],
]

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def fill (office, direction, x, y):
    for i in direction :
        nx = x
        ny = y
        while 0 <= n < nx and 0 <= n < ny :
            nx += dx[i]
            ny += dy[i]

        if office[nx][ny] == 6 :
            break
        #감시
        elif office[nx][ny] == 0 :
            office[nx][ny] = -1

def dfs(depth, office) :
    global min_value
    if depth == len(cctv) :
        cnt = 0
        for i in range(n) :
            count += office[i].count(0)
        min_value = min(min_value, cnt)


for i in range (n) :
    data = list(map(int,input().split()))
    office.append(data)
    for j in range (m) :
        if data[j] in [1, 2, 3, 4, 5] :
            cctv.append(data[j], i, j)


print(*office)



def dfs (graph, v) :
    print("1")