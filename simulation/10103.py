import sys
input = sys.stdin.readline
n = int(input())
a , b = 100, 100
for i in range (n) :
    dice1, dice2 = map(int,input().split())
    if dice1 > dice2 :
        b -= dice1
    elif dice1 < dice2 :
        a -= dice2
print(a)
print(b)  