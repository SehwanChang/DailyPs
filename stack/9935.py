import sys
input = sys.stdin.readline
word_1 = list(input().strip())
bomb = list(input().strip())
ans = []
for char in word_1 :
    ans.append(char)
    if ans[len(ans) - len(bomb) : len(ans)] == bomb :
        for _ in range(len(bomb)) :
            ans.pop()

if ans :
    print(''.join(ans))
else :
    print('FRULA')