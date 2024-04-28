import sys
input = sys.stdin.readline
from itertools import permutations
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
order = [i for i in range(1, 9)] 
score = float('-inf')

for x in permutations(order, 8): 
    x = list(x)
    hitter = x[:3] + [0] + x[3:] 
    number, point = 0, 0 
    for i in range(n): 
        out = 0 
        b1 = b2 = b3 = 0 
        while out < 3: 
            if graph[i][hitter[number]] == 0 :
               out += 1
            elif graph[i][hitter[number]] == 1 :
               point += b3
               b1, b2, b3 = 1, b1, b2
            elif graph[i][hitter[number]] == 2 :
                point += (b2 + b3)
                b1, b2, b3 = 0, 1, b1
            elif graph[i][hitter[number]] == 3 :
                point += (b1 + b2 + b3)
                b1, b2, b3 = 0, 0, 1
            elif graph[i][hitter[number]] == 4 :
                point += (b1 + b2 + b3) + 1 #타자까지 포함
                b1 = b2 = b3 = 0
            number += 1
            if number == 9 :
                number = 0
    score = max(score, point)

print(score)
