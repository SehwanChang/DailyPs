import sys
input = sys.stdin.readline
n = int(input())
buildings = list(map(int, input().split()))
nums = [i for i in range(n)]

ans = 0
for i in range(n):
    tmp = n - 1
    # 오른쪽 볼수 있는 빌딩.
    for right in range(i + 1, n):
        for k in range(i + 1, right):
            if buildings[k] - buildings[i] >= (buildings[right] - buildings[i]) / (right - i) * (k - i):
                tmp -= 1
                break

    # 왼쪽 볼 수 있는 빌딩.
    for left in range(0, i):
        for k in range(left + 1, i):
            if buildings[k] - buildings[left] >= (buildings[i] - buildings[left]) / (i - left) * (k - left):
                tmp -= 1
                break
    ans = max(tmp, ans)
print(ans)
#  (x1 , buildings[x1])
#  (x2, buildings[x2])


# y = ax + b

# 15
# 1 5 3 2 6 3 2 6 4 2 5 7 3 1 5
