import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
for i in range(t) :
    start, end = map(int, input().split())
    visited = set()
    q = deque([(start, "")])
    while q :
        num, command = q.popleft()
        if num == end :
            print(command)
            break
        if num not in visited :
            visited.add(num)
            q.append(((num * 2) % 10000, command + "D"))
            q.append(((num - 1) % 10000, command + "S"))
            q.append(( (num % 1000) * 10 + (num // 1000), command + "L"))
            q.append(( (num % 10) * 1000 + (num // 10), command + "R"))

# d : n *= 2, if n > 9999 : n = (n * 2) % 10000
# s : n -=1 if n == 0 : n = 9999
# l : 왼쪽 회전 1 2 3 4 -> 2 3 4 1
# r : 오른쪽 회전 1 2 3 4 -> 4 1 2 3 
# a = 1 2 3 4
# b = 3 4 1 2
# 1 2 3 4 -> 2 3 4 1 ->3 4 1 2 : 2번 (LL)
# 1 2 3 4 -> 4 1 2 3 -> 3 4 1 2 : 2번 (RR)
# 1 0 0 0 에 L 적용 : 0 0 0 1 (1)
# 1 0 0 0 에 R 적용 : 0 1 0 0 (100)