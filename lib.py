from itertools import permutations
from itertools import combinations
from itertools import product
import heapq
from bisect import bisect_left
from bisect import bisect_right
data = [1, 4, 5, 2, 2, 3, 19 , 192, 39]
arr = list(permutations(data, 3))
arr2 = list(product(data, repeat=3))

left = bisect_left(data, 2)
right = bisect_right(data, 2)
print(left, right)