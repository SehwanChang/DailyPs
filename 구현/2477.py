import sys
input = sys.stdin.readline
k = int(input())
distance = []
width = []
height = []
for i in range(6) :
    way, dist = map(int, input().split())
    distance.append((way, dist))
    if way == 1 or way == 2 :
        width.append(dist)
    else :
        height.append(dist)
lownum = []
for i in range(6) :
    if distance[i][0] == distance[(i + 2) % 6][0] :
        lownum.append(distance[(i + 1) % 6][1])

print( ((max(width)*max(height)) - (lownum[0]*lownum[1])) * k )