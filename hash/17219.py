import sys
n, m = map(int, input().split())
add = {}
for i in range(n) :
    site , pw = input().split()
    add[site] = pw
for i in range(m) :
    print(add[input().rstrip()])