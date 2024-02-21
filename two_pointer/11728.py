import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph_a = list(map(int, input().split()))
graph_b = list(map(int, input().split()))
res = graph_a + graph_b
res.sort()
print(*res)