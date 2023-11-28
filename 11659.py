import sys
input = sys.stdin.readline

n , m = map(int,input().split())
number = list(map(int,input().split()))
arr_sum = [0]
tmp = 0
for i in number :
    tmp += i
    arr_sum.append(tmp)
for i in range (m) :
    start , end = map(int,input().split())
    print(arr_sum[end] - arr_sum[start - 1])