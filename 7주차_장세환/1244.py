import sys
input = sys.stdin.readline
switch = int(input())
status = list(map(int,input().split()))

n = int(input())
for i in range(n) :
    sex, num = map(int,input().split())

    if sex == 1 :
        for j in range(num - 1, switch ,num) :
            status[j] = 1 - status[j]

    else:
        cnt = 0
        while (num-cnt-1 >= 1) and (num+cnt+1 <= n) and (switch[num-cnt-1] == switch[num+cnt+1]):
            cnt += 1
        for j in range(num-i, num+i+1):
            switch[j] = (switch[j]+1) % 2


n = int(input())
switch = [-1] + list(map(int, input().split()))
for _ in range(int(input())):
    sex, num = map(int, input().split())
    # 남자
    if sex == 1:
        i = 1
        while num*i <= n:
            switch[num*i] = (switch[num*i]+1) % 2
            i += 1
    # 여자
    else:
        i = 0
        while (num-i-1 >= 1) and (num+i+1 <= n) and (switch[num-i-1] == switch[num+i+1]):
            i += 1

        for j in range(num-i, num+i+1):
            switch[j] = (switch[j]+1) % 2

switch = switch[1:]
for i in range(0, switch, 20):
    print(*status[i:i+20])