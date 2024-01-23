import sys, heapq



def isEmpty(nums):
    for item in nums:
        if item[1] > 0:
            return False
    return True
t = int(input())
for _ in range(t) :
    k = int(input())
    min_heap = []
    max_heap = []
    nums = dict()
    for _ in range(k) :
        char, op = input().split()
        num = int(op)
        if char == 'I' :
            if num in nums :
                nums[num] += 1
            else :
                nums[num] = 1
                heapq.heappush(min_heap, num)
                heapq.heappush(max_heap, -num)
        elif char == 'D' :
            if not isEmpty(nums.items()) : 
                if num == 1 :
                    while -max_heap[0] not in nums or nums[-max_heap[0]] < 1 :
                        tmp = -heapq.heappop(max_heap)
                        if tmp in nums :
                            del(nums[tmp])
                    nums[-max_heap[0]] -= 1
                else :
                    while min_heap[0] not in nums or nums[min_heap[0]] < 1 :
                        tmp = heapq.heappop(min_heap)
                        if tmp in nums :
                            del(nums[tmp])
                    nums[min_heap[0]] -= 1
    if isEmpty(nums.items()) :
        print('EMPTY')
    else :
        while -max_heap[0] not in nums or nums[-max_heap[0]] < 1 :
            heapq.heappop(max_heap)
        while min_heap[0] not in nums or nums[min_heap[0]] < 1 :
            heapq.heappop(min_heap)
        print(-max_heap[0], min_heap[0])
