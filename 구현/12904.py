import sys
input = sys.stdin.readline
s = list(input().strip())
t = list(input().strip())
while True :
    if len(t) == len(s) :
        if s == t :
            print(1)
        else : 
            print(0)
        break
    char = t.pop()
    if char == 'B' :
        t = t[::-1]


# A
# AB
# BAB
# BABA
# ABABB






# B
# ABBA
# ABB
# BA
# B