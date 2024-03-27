import sys
input = sys.stdin.readline
s = input().strip()
stack = []
flag = False  
ans = ''
for char in s :
    if char == ' ' :
        while stack :
            ans += stack.pop()
        ans += char
    elif char == '<' :
        while stack :
            ans += stack.pop()
        flag = True
        ans += char
    elif char == '>' :
        flag = False
        ans += char
    elif flag :
        ans += char
    else : 
        stack.append(char)
while stack:
    ans += stack.pop()
print(ans)