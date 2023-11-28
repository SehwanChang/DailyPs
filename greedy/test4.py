import sys, time

n , k = map(int, input().split())
start_time = time.time()
cnt = 0
while n != 1 :
    if n % k != 0 :
        n -= 1
        cnt +=1
    else :
        n = n // k
        cnt += 1
    if n == 1: 
        break

end_time = time.time()
print(cnt)
print("시간 : ", end_time - start_time)