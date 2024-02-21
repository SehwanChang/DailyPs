import sys
from collections import defaultdict
input = sys.stdin.readline
n = int(input())
dic = {}
for _ in range(n) :
    book = input().strip()
    if book in dic.keys() :
        dic[book] += 1
    else :
        dic[book] = 1
sorted_items = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
print(sorted_items[0][0])