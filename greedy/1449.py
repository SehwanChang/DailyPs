import sys
input = sys.stdin.readline
n, l = map(int,input().split())
location = sorted(list(map(int,input().split())))
cnt = 1
cur = location[0]
for idx in range(1, len(location)) : 
    if cur - l <= location[idx] - 0.5 and location[idx] + 0.5 <= cur + l :
        continue
    else : 
        cnt += 1
        cur = location[idx]
print(cnt)


# 4 2
# 1 2 100 101

# 2

# 4 3
# 1 2 3 4
# 2

# 3 1
# 3 2 1
# 3
# 1 2 3