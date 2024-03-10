import sys
input = sys.stdin.readline
from itertools import combinations
from collections import deque
n = int(input())
arr = [i + 1 for i in range(n)]
population = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for i in range(n) :
    nums = list(map(int, input().split()))
    if len(nums) >= 2 :
        for j in range(len(nums)) :
            if j >= 1 :
                graph[i + 1].append((nums[j]))

def is_group(start, graph, candidate) :
    q = deque()
    q.append(start)
    cnt = 1
    visited = set()
    while q :
        x = q.popleft()
        visited.add(x)
        for next_node in graph[x] :
            if next_node in candidate and next_node not in visited :
                q.append(next_node)
                visited.add(next_node)
                cnt += 1
    return len(visited) == len(candidate)

res = float('inf')
for i in range(1, n // 2 + 1) :
    comb = combinations(range(1, n + 1), i)
    for group in comb :
        group_1 = list(group)
        #group2 : group_1 제외한 나머지
        group_2 = list(set(range(1, n + 1)) - set(group_1))
        #연결되어 있는지 여부 체크. 연결되어있다면 res 값 업데이트
        if is_group(group_1[0], graph, set(group_1)) and is_group(group_2[0], graph, set(group_2)) :
            sum_group1 = sum([population[i] for i in group_1])
            sum_group2 = sum([population[i] for i in group_2])
            res = min(res, abs(sum_group1 - sum_group2))
if res == float('inf') :
    print(-1)
else :
    print(res)
    

# 6 -> 구역의 개수 N
# 5 2 3 4 1 2 구역의 인구 
# 구역과 인접한 구역의 수, 인접한 구역의 번호 
# 2 2 4 
# 4 1 3 6 5 
# 2 4 2
# 2 1 3
# 1 2
# 1 2
#두 선거구로 못나누면 -1