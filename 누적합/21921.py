import sys
input = sys.stdin.readline
n, x = map(int, input().split())
nums = list(map(int, input().split()))
prefix = [0] * n
prefix[0] = nums[0]
vistied = []
for i in range(1, n) :
    prefix[i] = prefix[i - 1] + nums[i]
for i in range(n - x + 1) :
    tmp = prefix[i + x - 1] - prefix[i] + nums[i]
    vistied.append(tmp)
ans = max(vistied)
if ans == 0 :
    print('SAD')
    exit()
print(ans)
print(vistied.count(ans))

#여기까지는 일반적인 누적합 문제. 구간의 갯수는 ?

# 5 2
# 1 4 2 5 1
# 구간이 2 : 5, 6, 7, 3


#최대 방문자 0명 : SAD 출력
# 최대 방문자 
# 기간