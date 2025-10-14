import sys
sys.stdin = open('input.txt')

T = int(input())

arr = []

max_l = 0
min_l = 1000

max_h = 0
start = 0

max_index = 0

for _ in range(T):
    l, h = map(int, input().split())

    arr.append((h, l))

    # 시작점
    min_l = min(l, min_l)
    # 끝점
    max_l = max(l, max_l)
    # 최대 높이
    max_h = max(h, max_h)

arr = sorted(arr)

while arr:
    h, l = arr.pop()


        
            











    


