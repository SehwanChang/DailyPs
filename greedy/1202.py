import sys, heapq
input = sys.stdin.readline
n, k = map(int, input().split())
jewel = [list(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]

jewel.sort(key=lambda x: x[0])
bags.sort()

heap = []
ans = 0
idx = 0
for bag_weight in bags : 
    while idx < n and jewel[idx][0] <= bag_weight :
        #max_heap이기 때문에 min_heap에서 -를 붙여서 push.
        heapq.heappush(heap, -jewel[idx][1])
        idx += 1
    print('heap: ',heap)
    if heap :
        ans += -heapq.heappop(heap)

print(jewel)
print(bags)
print(ans)
# print(ans)
            
#보석 : n개 
#보석무게, 가격 m, v
#가방 : k개, 1개의 보석만 가능 , 가방 용량 = c
#훔칠 수 있는 보석의 최대 가격 구하기
