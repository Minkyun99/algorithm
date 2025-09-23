# 간단한 소인수분해
import sys
sys.stdin = open('input2.txt')

T = int(input())
 
for time in range(1, T+1):
    N = int(input())
    is_True = True
    arr = [0] * 5
    while is_True:
        if N % 2 == 0:
            N /= 2
            arr[0] += 1
        elif N % 3 == 0:
            N /= 3
            arr[1] += 1
        elif N % 5 == 0:
            N /= 5
            arr[2] += 1
        elif N % 7 == 0:
            N /= 7
            arr[3] += 1
        elif N % 11 == 0:
            N /= 11
            arr[4] += 1
        else:
            is_True = False
         
    print(f'#{time}',end=' ')
    for i in arr:
        print(i, end=' ')
    print()