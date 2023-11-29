# 서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?
# 첫째 줄에 자연수 S(1 ≤ S ≤ 4,294,967,295)가 주어진다.
# 첫째 줄에 자연수 N의 최댓값을 출력한다.
# 200
# 50
import sys
input = sys.stdin.readline
s = int(input())
total = 0
cnt = 0
while True :
    cnt += 1
    total += cnt
    if total > s :
        break
print(cnt - 1)


# n (n + 1) = 2 * s