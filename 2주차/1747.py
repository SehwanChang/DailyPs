import math

def isprime(x) :
    for i in range(2, int(x ** 0.5) + 1 ) :
        if x % i == 0 :
            return -1
    return 1
n = int(input())
result = 0
for i in range(n, 1000001) :
    if i == 1 : 
        continue
    if str(i) == str(i)[::-1]:
        if isprime(i) == 1 :
            result = i
            break
if result == 0 :
    result = 1003001
print(result)