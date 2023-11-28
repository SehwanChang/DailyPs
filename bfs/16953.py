from collections import deque
a, b = map(int,input().split())
q = deque([(a, 1)])

while q :
    tmp, cnt = q.popleft()
    if tmp > b :
        continue
    if tmp == b :
        print(cnt)
        break
    q.append((int(str(tmp) + "1"), cnt + 1))
    q.append((tmp * 2, cnt + 1))
else :
    print(-1)