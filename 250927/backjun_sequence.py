import sys
sys.stdin = open('input.txt')

# 인자 받기
T = int(input())
arr = list(map(int, input().split()))

# 배열 길이 지정
l = len(arr)

# count 선언 : 정방향으로 진행할 때, 만약 수열이라면, +1 하여 갯수를 셈
count = 1
# reverse_count 선언 : 역방향으로 진행할 때, 만약 수열이라면, +1 하여 갯수를 셈
reverse_count = 1
# result_count 선언 : 가장 큰 수열 값을 저장함
result_count = 0

# 순회하면서 수열 확인하는 for문
for i in range(l-1):
    # 정방향 순열 확인
    if arr[i] <= arr[i+1]:
        count += 1
    else:
        result_count = max(count, reverse_count, result_count)
        count = 1

    # 역방향 순열 확인
    if arr[i] >= arr[i+1]:
        reverse_count += 1
    else:
        result_count = max(count, reverse_count, result_count)
        reverse_count = 1

# 마지막 result_count 갱신
result_count = max(count, reverse_count, result_count)

print(result_count)


