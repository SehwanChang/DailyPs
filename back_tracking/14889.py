import sys
from itertools import combinations
input = sys.stdin.readline
n = int(input())
people = [i for i in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]
nums = list(combinations(people, n // 2))

gap = 100000000

def cal_sum (arr) :
    tmp = 0
    for i in combinations(arr, 2) :
        a, b  = i[0], i[1]
        tmp += (graph[a][b] + graph[b][a])
    return tmp

for num in nums :
    team_1, team_2 = 0, 0
    other_team = list(set(people) - set(num))
    # other_team = [i for i in people if i not in num]

    team_1 = cal_sum(num)
    team_2 = cal_sum(other_team)

    if gap > abs(team_2 - team_1) :
        gap = abs(team_2 - team_1)
print(gap)  