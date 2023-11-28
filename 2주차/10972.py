# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline
n = int(input())
p = list(map(int,input().split()))
for i in range(n - 1, 0 , -1) : #p의 맨 뒤 기준으로 오름차순인지 비교 
    if p[i]  > p[i - 1] : # 뒤 > 앞 : 1 4 3 2    -> 2 1 3 4
        for j in range(n - 1, 0 , -1) :
            if p[j] > p[i - 1] : 
                p[j] , p[i - 1] = p[i - 1], p[j]    #예시 : 1과 2 스왑 : 2 | 4 3 1 
                p = p[:i] + sorted(p[i:])
                print(*p)
                exit()
print(-1)