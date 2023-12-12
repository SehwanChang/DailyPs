import sys
from collections import deque
n, k = map(int, input().split())
q = deque(range(1, n + 1))
answer = [] 
while q :
    #rotate 가 음수 = 왼쪽방향, 양수 = 오른쪽방향 회전
    q.rotate(-k + 1)
    answer.append(q.popleft())
print("<"+", ".join(map(str, answer))+">")

#3, 6, 2, 7, 5, 1, 4
