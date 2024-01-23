'''
() -> 기본 VPS
x가 VPS라면 (x) -> VPS
(())() -> VPS

VPS를 판단해라 YES, NO

'''

from collections import deque

t = int(input()) # 테스트케이스

for i in range(t):
    Queue = deque()
    word = input()
    flag = True
    for j in word:
        if j == '(':
            Queue.append(j)
        elif j == ')':
            if len(Queue) == 0:
                print('NO')
                flag = False
                break
            Queue.pop()
    if flag:
        if len(Queue) == 0:
            print('YES')
        else:
            print('NO')



'''

'''

