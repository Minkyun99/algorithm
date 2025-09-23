# 5789. 현주의 상자 바꾸기 
import sys
sys.stdin = open('input1.txt')
T = int(input())

for time in range(1, T+1):
    Q, N = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = [0] * Q

    for i in range(N):
        start = arr[i][0]
        end = arr[i][1]

        for j in range(start-1, end):
            result[j] = i + 1
    print(f'#{time}', end=' ')
    for x in result:
        print(f'{x}', end=' ')
    print()