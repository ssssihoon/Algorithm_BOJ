'''
재현이가 잘못된 수를 부를때마다 0을 외친다
그 후 가장 최근 수를 ㅈㅣ운다.
이렇게의 모든 수의 합을 알고싶다

'''


import sys
from collections import deque

Queue = deque()
input = sys.stdin.readline

k = int(input())

for i in range(k):
    num = int(input())
    if num != 0:
        Queue.append(num)
    else :
        Queue.pop()

print(sum(Queue))



