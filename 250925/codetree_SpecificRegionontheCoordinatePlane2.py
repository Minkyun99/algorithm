import sys
sys.stdin = open('input2.txt')

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]


def find(idx, result):
    global result_result, result_min_area
    
    if idx == n:
        if len(result) == 3:
            max_x_result = max(x[result[0]], x[result[1]], x[result[2]])
            min_x_result = min(x[result[0]], x[result[1]], x[result[2]])

            max_y_result = max(y[result[0]], y[result[1]], y[result[2]])
            min_y_result = min(y[result[0]], y[result[1]], y[result[2]])

            result_min_area = min(result_min_area, (max_x_result-min_x_result)*(max_y_result-min_y_result))
        return
    
    find(idx+1, result)
    find(idx+1, result+[idx])

result_result = []
result_min_area = 40000*40000
find(0, [])
print(result_min_area)




