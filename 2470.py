import sys 
input = sys.stdin.readline
n = int(input())
ans = []
solution = sorted(list(map(int, input().split())))
start, end = 0, n - 1
tmp = float('inf')
while start < end :
    res = solution[start] + solution[end]
    if abs(res) < tmp :
        tmp = abs(res)
        x = solution[start]
        y = solution[end]
    if res < 0 :
        start += 1
    else :
        end -= 1
print(x, y)
