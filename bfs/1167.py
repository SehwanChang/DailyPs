a, b, c = map(int, input().split())
def power(a, b) :
    if b == 1 :
        return a % c
    else :
        tmp = power(a, b // 2)
        if b % 2 == 0 :
            return tmp * tmp % c
        else :
            return tmp * tmp * a % c
res = power(a, b)
print(res)