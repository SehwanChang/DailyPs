import sys
input = sys.stdin.readline
n , m = map(int,input().split())
res = 0
for i in range (n) :
    data = list(map(int,input().split()))
    res = max(min(data),res)
print(res)