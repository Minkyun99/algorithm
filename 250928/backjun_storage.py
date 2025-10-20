# import sys
# sys.stdin = open('input.txt')

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


sort_arr = sorted(arr)
print(sort_arr)

max_idx = sort_arr[-1][0]
max_h = sort_arr[-1][1]
total_square = (max_l - min_l) * max_h

left_arr = []
right_arr = []

for h, l in sort_arr:
    if l < max_idx:
        left_arr.append((l, h))
    else :
        right_arr.append((l, h))

left_arr = sorted(left_arr)
right_arr = sorted(right_arr)

max_len = left_arr[0][1]
idx = l
left_max_h = max_h
left_max_i = max_idx
while left_max_i >= min_l:
    if left_max_i < min_l:
        break
    for i in range(len(left_arr)-1):
        if max_len <= left_arr[i][0] :
            max_len = left_arr[i][1]
            idx = left_arr[i][0]
            remove_item = i
    left_arr.pop(remove_item)
    small_sqaure = (left_max_h - max_len) * (left_max_i - idx)

    for j in range(len(left_arr)-1):
        if left_arr[j][0] > idx:
            left_arr.pop(j)

    left_max_h = max_len
    left_max_i = idx


    


        
            











    


