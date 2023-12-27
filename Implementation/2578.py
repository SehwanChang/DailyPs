import sys
input = sys.stdin.readline
from collections import deque
cnt = 0
graph = [list(map(int, input().split())) for _ in range(5)]
sheet = [list(map(int, input().split())) for _ in range(5)]
bingo = [[False] * 5 for _ in range(5)]
graph_q = deque()
q = deque()
for i in range(5) :
    for num in graph[i] :
        graph_q.append(num)
for i in range(5) :
    for num in sheet[i] :
        q.append(num)

def isBingo(bingo):
    cnt = 0
    for i in range(5) :
        if all(bingo[i][j] for j in range(5)) :
            cnt += 1
    for j in range(5) :
        if all(bingo[i][j] for i in range(5)) :
            cnt += 1
    if all(bingo[i][i] for i in range(5)) :
        cnt += 1
    if all(bingo[i][4 - i] for i in range(5)) :
        cnt += 1

    return cnt >= 3


cnt = 0
while q :
    num = q.popleft()
    cnt += 1
    tmp = graph_q.index(num)
    bingo[tmp // 5][tmp % 5] = True
    if isBingo(bingo) :
        print(cnt)
        break
