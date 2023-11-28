n = int(input())
check = n
count = 0
while True :
    check =(check % 10) *10 + ((check % 10) + (check // 10)) % 10
    count +=1
    if n == check :
        break
print(count)