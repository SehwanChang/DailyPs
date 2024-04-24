import sys
input = sys.stdin.readline
n , l = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]


def isPath(arr) :
    bridge = [False] * (n)
    for i in range(n - 1):
        
        if abs(arr[i] - arr[i + 1]) > 1 :
             return False
        #내리막길
        elif arr[i] > arr[i + 1] :
            tmp = arr[i + 1]
            for j in range(i + 1, i + l + 1) : # l개만큼 탐색.
                if 0 <= j < n :
                    if arr[j] != tmp or bridge[j]  :
                        return False
                    bridge[j] = True   
                else :
                     return False
        #오르막길
        elif arr[i] < arr[i + 1] :
            tmp = arr[i]
            for j in range(i, i - l, -1) :
                if 0 <= j < n :
                     if arr[j] != tmp or bridge[j]:
                         return False
                     bridge[j] = True
                else : 
                     return False
    return True

cnt = 0
for row in graph :
    if isPath(row) :
            cnt += 1

for j in range(n):
    col = [graph[i][j] for i in range(n)]
    if isPath(col):
        cnt+=1
print(cnt)