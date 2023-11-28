import sys
input = sys.stdin.readlines
n, m = map(int,input().split())
#왼쪽  위 오른쪽 아래 
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]