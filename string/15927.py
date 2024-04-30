import sys
import math
input = sys.stdin.readline

s = input().strip()
l = len(s)
# 길이 1 or 같은문자만 반복
if s == s[0] * l:
    print(-1)
elif s[:l//2][::-1] == s[math.ceil(l/2):]:
    print(l-1)
else:
    print(l)
