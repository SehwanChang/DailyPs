import sys, heapq
input = sys.stdin.readline
heap = []
max_day = 0
n = int(input())
for _ in range(n) :
    d, w = map(int, input().split())
    heapq.heappush(heap, (-w, d)) #최대 힙이기 때문에 점수를 음수로 할당
    max_day = max(max_day, d)
assigned = [False] * (max_day + 1)
ans = 0
while heap : 
    w, d = heapq.heappop(heap)
    w = - w #점수 다시 양수로 처리 
    #최대 스코어를 마지막날부터 비어있는 곳에 할당.
    for i in range(d, 0, -1) :
        if assigned[i] :
            continue
        assigned[i] = True
        ans += w
        break
print(ans)
#d: 마감남은일 수 , w : 과제 점수
#하루에 한 과제 끝내기 가능. 

# 7
# 4 60
# 4 40
# 1 20
# 2 50
# 3 30
# 4 10
# 6 5

# 30 50 40 60 5 