n = int(input())
arr_quiz = []
arr_answer = []
one = 0
answer = ''
front = ''
back = ''

for i in range(n):
    li = input()
    arr_quiz.append(li)

q_idx = arr_quiz.index('?') # ?물음표가 있는 인덱스

if 0 < q_idx < n-1:
    front = arr_quiz[q_idx-1][-1] # 맨 앞 알파벳으로 와야할 것
    back = arr_quiz[q_idx+1][0] # 맨 뒤 알파벳으로 와야할 것
elif q_idx == 0 and n >= 2:
    back = arr_quiz[q_idx + 1][0]
elif q_idx == n-1 and n >= 2:
    front = arr_quiz[q_idx-1][-1]
elif n == 1:
    one += 1

m = int(input())

for k in range(m):
    li_t = input()
    arr_answer.append(li_t)

for j in range(m):
    if ((arr_answer[j] not in arr_quiz) and arr_answer[j][0] == front) and ((arr_answer[j] not in arr_quiz) and arr_answer[j][-1] == back):
        answer = arr_answer[j]
        break
    elif ((arr_answer[j] not in arr_quiz) and arr_answer[j][0] == front) or ((arr_answer[j] not in arr_quiz) and arr_answer[j][-1] == back):
        answer = arr_answer[j]
    elif one == 1:
        answer = arr_answer[j]
print(answer)