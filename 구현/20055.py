import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())
belt = deque(map(int, input().split()))
robot = deque([0] * n)
ans = 0
while True :
    ans += 1
    #벨트 회전
    belt.rotate(1)
    robot[-1] = 0
    robot.rotate(1)
    robot[-1] = 0
    #로봇 이동 : 다음 로봇이 비어있어야함, 내구도 >= 1
    for i in range(n - 2, -1, -1) :
        if belt[i + 1] >= 1 and robot[i + 1] == 0 and robot[i] == 1:
            robot[i + 1] = 1
            robot[i] = 0
            belt[i + 1] -= 1
    #항상 마지막 로봇: 내려야함
    robot[-1] = 0
    #로봇 올리기
    if belt[0] != 0 and robot[0] != 1:
        robot[0] = 1
        belt[0] -= 1
    #종료 조건 체크
    if belt.count(0) >= k :
        break
print(ans)



# 3 2
# 1 2 1 2 1 2
# 2
