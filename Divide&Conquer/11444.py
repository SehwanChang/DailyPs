import sys
input = sys.stdin.readline
n = int(input())
matrix = [[1, 1], [1, 0]]

def mul_matrix(a, b) :
    res = [[0] * 2 for _ in range(2)]
    for i in range(2) :
        for j in range(2) :
            for k in range(2) :
                #a11 b11 + a12 b21
                res[i][j] = (res[i][j] +  (a[i][k] * b[k][j]) % 1000000007) % 1000000007
    return res

def power(a, b) :
    if b == 1 :
        return a
    else :
        tmp = power(a, b // 2)
        if b % 2 == 0 :
            return mul_matrix(tmp, tmp)
        else :
            return mul_matrix(mul_matrix(tmp, tmp), a)
        
result = power(matrix, n)
print(result[0][1] % 1000000007)