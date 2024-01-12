import sys
input = sys.stdin.readline
graph = [input().strip() for _ in range(4)]
k = int(input())
orders = [list(map(int, input().split())) for _ in range(k)]
ans = 0 
def rotate(s, direction) : 
    if direction == 1 : #시계방향
        return s[-1 :] + s[ :-1]
    else : #반시계 방향 
        return s[1:] + s[0]        

for order in orders :
    num, direction = order[0] - 1, order[1]
    rotate_direction = [0] * 4
    rotate_direction[num] = direction

    for i in range(num, 3) : #자기 기준 오른쪽
        if graph[i][2] != graph[i + 1][6] : 
            rotate_direction[i + 1] = -rotate_direction[i]
    for i in range(num, 0, -1) : #자기 기준 왼쪽 
        if graph[i][6] != graph[i -1][2] : 
            rotate_direction[i - 1] = -rotate_direction[i]
    
    for i in range(4) :
        if rotate_direction[i] != 0 :
            graph[i] = rotate(graph[i], rotate_direction[i])
for i in range(4) :
    ans += (2 ** i ) if graph[i][0] == '1' else 0
print(ans)

# 결과를 계속 업데이트해야하는 상황이 아니면 자기 기준 오른쪽 쭉 업데이트, 자기 기준 왼쪽 쭉 업데이트 
