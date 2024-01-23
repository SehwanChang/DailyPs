from itertools import permutations
n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
combi = list(permutations(num, m))
for i in combi :
    print(*i)