# 백준 2477.참외밭

import sys
sys.stdin = open('input1.txt')

N = int(input())

direction = []
distance = []

result_direc = []

for _ in range(6):
    a, b = map(int, input().split())
    direction.append(a)
    distance.append(b)

for direc in range(6):
    if direction[(direc - 1 + 6) % 6] == direction[(direc+1)%6]:
        result_direc.append(direc)

row_result = 0
col_result = 0
for i in range(6):
    if direction[i] == 1 or direction[i] == 2:
        row_result = max(distance[i], row_result)
    elif direction[i] == 3 or direction[i] == 4:
        col_result = max(distance[i], col_result)

big_area = row_result * col_result
small_area = distance[result_direc[0]] * distance[result_direc[1]]
total_melon = (big_area - small_area) * N

print(total_melon)

    



    

