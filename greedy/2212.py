import sys
input = sys.stdin.readline
n = int(input())
k = int(input())
sensors = sorted(list(map(int, input().split())))
gaps = []
for i in range(n - 1) :
    gaps.append(sensors[i + 1] - sensors[i])

gaps.sort()
print(sum(gaps[ : n - k]))

#1 3 6 6 7 9
#    0     2         0         3       2
# [3,// 6, 7, 8,// 10, //12 14, 15,// 18, 20]
# [1, 1, 1, 2, 2] 
# [2, 2, 3, 3]
# 7
#