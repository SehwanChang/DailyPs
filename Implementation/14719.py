import sys
input = sys.stdin.readline
h, w = map(int, input().split())
rain = list(map(int, input().split()))
ans = 0
for i in range(1, w - 1) :
    left = max(rain[: i])
    right = max(rain[i + 1 :])
    tmp = min(left, right)
    if tmp > rain[i] :
        ans += tmp - rain[i]
print(ans)

# 3 6
# 5 4 1 3 1 2

#예시 : 
#왼쪽 최대 = 5 , 오른쪽 최대 = 4
#그러면 tmp = 4로됨 , 만약 현재 높이가 4보다 작으면 
# 4 와의 차이 합.