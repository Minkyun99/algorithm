# 구간 중 최대합
import sys
sys.stdin = open('input3.txt')
n, k = map(int, input().split())
arr = list(map(int, input().split()))

max_value = 0
for i in range(n-k+1):
    result = 0
    for j in range(i, i+k):
        result += arr[j]
    max_value = max(result, max_value)

print(max_value)