import sys
sys.stdin = open('input4.txt')

n, k = map(int, input().split())
x = []
c = []

max_pos = 0

for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)
    max_pos = max(max_pos, int(pos))

arr = [''] * (max_pos+1)

for i in range(n):
    arr[x[i]] = c[i]

max_value = 0
max_count = 0
if k > max_pos+1:
    for i in c:
        if i == 'H':
            max_count += 2
        elif i == 'G':
            max_count += 1
    print(max_count)
else:
    for i in range(len(arr)-k):
        count = 0
        for j in range(i, i+k+1):
            if arr[j] == 'H':
                count += 2
            elif arr[j] == 'G':
                count += 1
        max_value = max(max_value, count)

    print(max_value)