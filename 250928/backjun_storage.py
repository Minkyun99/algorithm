import sys
sys.stdin = open('input.txt')

T = int(input())
arr = [0] * 1000

max_l = 0
min_l = 1000

max_h = 0
start = 0

for _ in range(T):
    l, h = map(int, input().split())

    arr[l] = h
    min_l = min(l, min_l)
    max_l = max(l, max_l)
    max_h = max(h, max_h)

for i in range(1000):
    


