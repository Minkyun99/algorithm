import sys
sys.stdin = open('input1')

candidate = int(input())
N = int(input())

arr = list(map(int, input().split()))
student = [0] * (N+1)
candidate_student = [0] * candidate
print(candidate_student)
is_True = True

# order = [i for i in range(candidate)]

order = [0] * (N+1)
[0,2,1,4,3,5,0,0]
idx = 0
index = 0

def find(t):
    global student, candidate_student
    for j in range(len(candidate_student)):
        if student[t] >= student[candidate_student[j]]:
            result = 100
            for k in range(len(order)):
                if order[k] > 0:
                    result = min(result, order[k])
                    index = k
            student[index] = 0
            candidate_student[j] = t
            return


while arr:
    t = arr.pop(0)
    student[t] += 1
    if 0 not in candidate_student:
        find(t)
    else:
        if t not in candidate_student:
            for i in range(len(candidate_student)):
                if candidate_student[i] != 0: # 누가 있으면 continue
                      # 자리가 꽉 찼을 경우
                    continue
                elif candidate_student[i] == 0:  # 누가 없으면 그 자리에 넣고 break
                    candidate_student[i] = t
                    order[t] = idx
                    idx += 1
                    break
            # 자리가 꽉 찼을 경우
            # elif student[t] >= student[candidate_student[i]]:
            #     student[candidate_student[i]] = 0
            #     candidate_student[i] = t
            #     break


print(candidate_student)
