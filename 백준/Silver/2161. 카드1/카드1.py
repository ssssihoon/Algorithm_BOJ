'''
1. 제일 위에 있는 카드를 바닥에 버린다
2. 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.

버린 카드들을 순서대로 출력, 마지막 남게 되는 카드 출력
'''

'''
현재 입력 7
1
2
3
4
5
6
7
'''
from collections import deque

Queue = deque()

n = int(input())

left_li = []

for i in range(1, n+1):
    Queue.append(i)

while len(Queue) != 1:
    left_li.append(Queue.popleft())
    Queue.append(Queue.popleft())

left_li = list(left_li)

print(*left_li ,Queue[0])