import heapq
n = int(input())
array = [list(map(int, input().split()) for _ in range(n))]
array.sort()

queue = []

for i in array:
    heapq.heappush(queue, i[1])
    if i[0] < len(queue):
        heapq.heappop(queue)
    
print(sum(queue))