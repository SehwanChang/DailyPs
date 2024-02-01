import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
word = []
ans = set()
def backtracking(idx) :
    if len(word) == m :
        word_tuple = tuple(word)
        if word_tuple not in ans:
            print(*word)
            ans.add(word_tuple)
        return
    
    for i in range(idx, n) :
        word.append(nums[i])
        backtracking(i)
        word.pop()
backtracking(0)
