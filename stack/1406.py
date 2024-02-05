import sys
input = sys.stdin.readline
from collections import deque
left = list(input().strip())
right = []
m = int(input())
for i in range(m) :
    command = list(input().split())
    if command[0] == 'L' and left :
        right.append(left.pop())
    elif command[0] == 'D' and right :
        left.append(right.pop())
    elif command[0] == 'B' and left :
        left.pop()
    elif command[0] == 'P' :
        left.append(command[1])
answer = left + right[::-1]
print(''.join(answer))

#핵심 : 시간초과에 걸리지 않으려면 2가지 스택을 활용해서 커서가 이동하는것처럼 효과를 내야한다!




# 길이 l인 문자열 : 커서 경우의 수 l + 1가지
# L : 왼쪽으로 이동, 문장 맨 앞 = 무시 
# D : 오른쪽, 문장 맨 뒤 = 무시 
# B : 왼쪽 문자 삭제, 문장 맨 앞 = 무시 
# P $ : $라는 문자 커서 왼쪽 추가 

#초기값 = 문장 맨 오른쪽  

#abcd
#abcdx
#abcdy
    
#abc 
    #처음 커서 위치 = 2
#L   abc , 커서 = 1
#L   abc , 커서 = 0
#L   abc , 커서 = -1 : 맨앞
#L   abc , 커서 = -1
#L 
#P x xabc , 커서 = 0
# L  xabc, 커서 = 1
# B  xabc, 커서 = 0
# P y yxabc, 커서 = 1







#커서위치 = 3
# dmih
# 11
# B : dmi, cur = 2, i 뒤에 존재
# B : dm, cur = 1, m 뒤에 존재 
# P x : dmx, cur = 2, x 뒤에 존재
# L : dmx, cur = 1, m 뒤에 존재
# B : dx, cur = 0, d 뒤에 존재 
# B : x, cur = -1
# B : x, cur = -1
# P y : yx cur = 0
# D : yx cur = 1
# D : yx cur = 1
# P z : yxz cur = 2
