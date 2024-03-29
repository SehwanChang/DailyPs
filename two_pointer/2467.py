import sys
input = sys.stdin.readline
n = int(input())
solution = list(map(int, input().split()))
solution.sort()
start, end = 0, n - 1
ans_left, ans_right = start, end
ans = abs(solution[start] + solution[end])
while start < end :
    tmp = solution[start] + solution[end]
    if abs(tmp) < ans :
        ans_left = start
        ans_right = end
        ans = abs(tmp)
        if ans == 0 :
            break
    if tmp < 0 :
        start += 1
    else : 
        end -= 1
print(solution[ans_left], solution[ans_right])