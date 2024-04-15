k = int(input())
signs = list(input().split())
visited = [0] * 10
def check(a, b, op):
  if op == '<':
    if a > b: return False
  if op == '>':
    if a < b: return False
  return True

def dfs(cnt, num):
  if cnt == k + 1:
    answer.append(num)
    return
  
  for i in range(10):
    if visited[i]: continue

    if cnt == 0 or check(num[cnt - 1], str(i), signs[cnt - 1]):
      visited[i] = 1
      dfs(cnt+1, num+str(i))
      visited[i] = 0


answer = []
dfs(0, '')
answer.sort()
print(answer[-1])
print(answer[0])