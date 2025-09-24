import sys
sys.stdin = open('input1.txt')

N = int(input())
a, b, c = map(int, input().split())

arr = [i+1 for i in range(N)]
result_result = []
result = [0] * 3
print(result)

result = []
for i in range(N):
    for j in range(N):
        for h in range(N):
            result = [arr[i], arr[j], arr[h]]
            result_result.append(result)

result_count = 0
for x in range(len(result_result)):
    if result_result[x][0] > 3 and result_result[x][1] > 4 and result_result[x][2] > 5: 
        result_count += 1

print((N*N*N) - result_count)


    