import sys
input = sys.stdin.readline
ans = 0
s = input().strip()
while True:
    ans += 1
    num = str(ans)
    while len(num) > 0 and len(s) > 0:
        if num[0] == s[0]:
            s = s[1:]
        num = num[1:]
    if s == '':
        print(ans)
        break
