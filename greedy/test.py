from random import randint
import time

array = []
for i in range(10000) : 
    array.append(randint(1, 100))

start_time = time.time()

for i in range(len(array)) :
    min_idx = i
    for j in range(i + 1, len(array)) :
        if array[min_idx] > array[j] :
            min_idx = j
    array[i], array[min_idx] = array[min_idx] , array[i]
end_time = time.time()
print("선택정렬 성능: ",end_time - start_time)
array = []
for i in range(10000) : 
    array.append(randint(1, 100))

start_time = time.time()
array.sort()
end_time = time.time()
print("라이브러리 성능 : ",end_time - start_time)