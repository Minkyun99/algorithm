import sys
sys.stdin = open('input.txt')

T = int(input())

max_l = 0
min_l = 1000

max_h = 0
start = 0

max_index = 0
arr = [0] * 1001

for _ in range(T):
    l, h = map(int, input().split())
    # 시작점
    min_l = min(l, min_l)

    # 끝점
    max_l = max(l, max_l)
    arr[l] = h

left_arr = []
right_arr = []

max_value = max(arr)
max_index = arr.index(max_value)

total_square = ((max_l+1) - min_l) * max_value

for i in range(min_l, max_l+1):
    if i < max_index:
        left_arr.append(arr[i])
    else:
        right_arr.append(arr[i])


# 가장 높은 기둥을 기준으로 왼쪽
result_left_idx = max_index - min_l

while len(left_arr) > 0:
    max_left = max(left_arr)
    max_left_index = left_arr.index(max_left)

    if max_left_index == 0:
        small_sqaure = (max_value - max_left) * result_left_idx
        total_square = total_square - small_sqaure
        left_arr = []
        break

    left_arr = left_arr[0:max_left_index]
    
    small_sqaure = (max_value - max_left) * (result_left_idx - max_left_index)
    total_square = total_square - small_sqaure
    result_left_idx = max_left_index


# 가장 높은 기둥을 기준으로 오른쪽
result_right_idx = (max_l+1) - (max_index+1)

right_arr.pop(0)

while len(right_arr) > 0:
    max_right = max(right_arr)
    max_right_index = right_arr.index(max_right)

    if max_right_index == len(right_arr)-1:
        small_sqaure = (max_value - max_right) * result_right_idx
        total_square = total_square - small_sqaure
        right_arr = []
        break


    if max_right == max_value:
        right_arr = right_arr[max_right_index+1:len(right_arr)]
        result_right_idx = len(right_arr)
    
    else:
        right_arr = right_arr[max_right_index+1:len(right_arr)]   
        small_sqaure = (max_value - max_right) * (result_right_idx - max_right_index)
        total_square = total_square - small_sqaure
        result_right_idx = max_right_index
        

print(total_square)