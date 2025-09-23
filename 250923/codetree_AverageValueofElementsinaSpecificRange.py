import sys
sys.stdin = open('input5.txt')

n = int(input())
arr = list(map(int, input().split()))

def find(idx, i):
    global count

    if len(i) > 2:
        return

    if idx ==n:
        result_result =0
        if len(i) == 2:
            start, end = i[0], i[1]
            for j in range(start, end+1):
                result_result += arr[j]
                count += 1
        return 

    find(idx+1, i)
    find(idx+1, i + [idx])

count = n
find(0, [])
print(count)