import sys
input = sys.stdin.readline
n = int(input())
graph = [list(map(str, input().strip())) for _ in range(n)]


def check_graph():
    max_cnt = 0
    for i in range(n):
        tmp = 1
        for j in range(n - 1):
            if graph[i][j] == graph[i][j + 1]:
                tmp += 1
            else:
                tmp = 1
            max_cnt = max(tmp, max_cnt)
        tmp = 1
        for j in range(n - 1):
            if graph[j][i] == graph[j + 1][i]:
                tmp += 1
            else:
                tmp = 1
            max_cnt = max(tmp, max_cnt)

    return max_cnt


res = 0
# 오른쪽, 아래쪽 swap
for i in range(n):
    for j in range(n - 1):
        tmp = 0
        # 오른쪽
        if j + 1 < n and graph[i][j] != graph[i][j + 1]:
            graph[i][j], graph[i][j + 1] = graph[i][j + 1], graph[i][j]
            tmp = check_graph()
            # 원상복구
            graph[i][j], graph[i][j + 1] = graph[i][j + 1], graph[i][j]
            res = max(tmp, res)
        tmp = 0
        # 아래
        if i + 1 < n and graph[i][j] != graph[i + 1][j]:
            graph[i][j], graph[i + 1][j] = graph[i + 1][j], graph[i][j]
            tmp = check_graph()
            # 원상복구
            graph[i][j], graph[i + 1][j] = graph[i + 1][j], graph[i][j]
            res = max(tmp, res)
print(res)

# 사탕의 색이 다른 인접한 2칸 고름
# 고른칸에 있는 사탕 서로 바꿈
# 같은색 색깔 모두 먹ㅇ므

# 5
# Y C P Z Y
# C Y Z Z P
# C C P P P
# Y C Y Z C
# C P P Z Z
