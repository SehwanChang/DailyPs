import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
broken = list(map(int, input().split()))


min_click  = abs(100 - n)
for channel in range(1000001) :
    channel_str = str(channel)
    for j in  range(len(channel_str)) :
        if int(channel_str[j]) in broken :
            break
        elif j == len(channel_str) - 1 :
            clicks = len(channel_str) + abs(int(channel_str) - int(n))
            min_click = min(min_click, clicks)
print(min_click)
