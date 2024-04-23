import sys
input = sys.stdin.readline
n = int(input())
honey = list(map(int, input().split()))
prefix = [0] * n
prefix[0] = honey[0]
for i in range(1, n) :
    prefix[i] = prefix[i - 1] + honey[i]

ans = 0
#꿀통 벌 벌 
for i in range(1, n - 1) :
    ans = max(ans, prefix[-2] + prefix[i - 1] - honey[i])
#벌 꿀통 벌 
for i in range(1, n - 1) :
    ans = max(ans, prefix[-2] - honey[0] + honey[i] )
# 벌1 ㅇ ㅇ ㅇ 꿀통 ㅇ ㅇ ㅇ 벌2 
#벌 벌 꿀통
for i in range(1, n - 1) :
    ans = max(ans, prefix[-1] - honey[0] + prefix[-1] - prefix[i] - honey[i])
print(ans)
#벌의 위치를 전부 고려할 필요가 없음 : 꿀통의 위치에 따라 벌은 자연스럽게 결정됨.