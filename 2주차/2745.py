base = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n , b = input().split()
result = 0

for i in range(len(n) - 1, -1, -1) :
    result += base.index(n[i]) * (int(b) ** (len(n) - 1 -i))
print(result)   