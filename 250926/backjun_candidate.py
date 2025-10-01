import sys
sys.stdin = open('input1.txt')

candidate = int(input())
N = int(input())

arr = list(map(int, input().split()))
student = [0] * (N+1)
candidate_student = [0] * candidate
is_True = True

# order = [i for i in range(candidate)]

order = [0] * (N+1)
idx = 1
index = 0
def find(t):
    global student, candidate_student, idx, order, index
    result = 100
    for j in range(len(candidate_student)):
        if student[t] >= student[candidate_student[j]]:
            for k in range(len(candidate_student)):
                result = min(result, order[candidate_student[k]])
            index = k
            candidate_student[k] = t
            order[t] = idx
            idx += 1
            # for c in range(len(candidate_student)):
            #     if candidate_student[c] :   
            #         pass
            
            
            
            # for k in range(len(order)):
            #     result = min(result, order[k]) 

            # candidate_student[j] = t


            print(candidate_student)
            print(order)
            return


while arr:
    t = arr.pop(0)
    student[t] += 1
    if 0 not in candidate_student:
        if t not in candidate_student:
            find(t)
    else:
        for i in range(len(candidate_student)):
            if candidate_student[i] == 0:
                candidate_student[i] = t
                print(t)
                order[t] = idx
                print(order)
                idx += 1
                break


print(candidate_student)
