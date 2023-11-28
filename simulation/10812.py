import sys
input = sys.stdin.readline
n, m = map(int, input().split())
res = [i + 1 for i in range(n)]
for i in range(m) :
    begin, end, mid = map(int,input().split())
    res = res[:begin - 1] + res[mid - 1 : end] + res[begin - 1: mid - 1] + res[end:]
print(*res)