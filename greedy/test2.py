import time
import sys
input = sys.stdin.readline
n , m , k = map(int,input().split())
# m :숫자가 더해지는 횟수 
# k : k번 초과해서 더할 수 없음.
data = list(map(int,input().split()))
data.sort(reverse=True)

res = 0
cnt = int(m / (k + 1) * k)
cnt += m % (k + 1)

res += cnt * data[0]
res += (m - cnt) * data[1]
print(res)