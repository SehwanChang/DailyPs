import heapq

heap = []

# 아래 for문을 실행하고 나면 heap은 [1,2,3,5,4]로 힙 정렬이 되게 된다.
for i in range(1,6):
	heapq.heappush(heap, i)
print(heap)
# 작은 숫자 순서대로 1,2,3,4,5가 출력된다.
for i in range(5):
	print(heapq.heappop(heap))