import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
items = list(map(int, input().split()))
items.sort()
start, end = 0, n - 1
cnt = 0
while start < end :
    tmp = items[start] + items[end]
    if tmp == m :
        cnt += 1
        start += 1
    elif tmp < m :
        start += 1
    else : 
        end -= 1
print(cnt)