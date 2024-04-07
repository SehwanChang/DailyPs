import sys
input = sys.stdin.readline
n = int(input())
positive = []
negative = []
ones = 0
for _ in range(n) :
    num = int(input())
    if num > 1 : 
        positive.append(num)
    elif num == 1 :
        ones += 1
    else :
        negative.append(num)
positive.sort(reverse=True)
negative.sort()

ans = 0
for i in range(0, len(positive) - 1, 2) :
    ans += positive[i] * positive[i + 1]
if len(positive) % 2 == 1 :
    ans += positive[-1]

for i in range(0, len(negative) - 1, 2) :
    ans += negative[i] * negative[i + 1]
if len(negative) % 2 == 1 :
    ans += negative[-1]
ans += ones
print(ans)