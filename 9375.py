import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t) :
    n = int(input())
    clothes = {}
    for _ in range(n) :
        item, type = input().split()
        if type not in clothes :
            clothes[type] = []
        clothes[type].append(item)
    cnt = 1
    for key in clothes :
        cnt *= (len(clothes[key]) + 1)
    print(cnt - 1)