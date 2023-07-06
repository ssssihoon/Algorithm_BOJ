import sys
from itertools import combinations
n = int(input())
sour = []
bitter = []
for _ in range(n):
    a, b = map(int, input().split())
    sour.append(a)
    bitter.append(b)

diff = float('inf')

for i in range(1, n+1):
    idxs = list(combinations(list(range(n)), i))

    for food in idxs:
        s = 1
        b = 0

        for j in range(i):
            s *= sour[food[j]]
            b += bitter[food[j]]
        if abs(s - b) < diff:
            diff = abs(s - b)

print(diff)

'''
import sys, itertools
from itertools import combinations # 중복되지 않는 조합형 이터레이터
input = sys.stdin.readline

n = int(input())
sour = []
bitter = []
for _ in range(n):
    a, b = map(int, input().split())
    sour.append(a)
    bitter.append(b)

diff = float('inf')

for i in range(1, n+1): # 재료를 i개 뽑을 때
    idxs = list(combinations(list(range(n)), i)) # 가능한 경우를 담은 리스트

    for food in idxs: # 경우 하나씩 탐색
        s = 1
        b = 0

        for j in range(i): # 맛 계산
            s *= sour[food[j]]
            b += bitter[food[j]]
        if abs(s - b) < diff:
            diff = abs(s - b)

print(diff)






N = int(input())
food_list_S = []
food_list_B = []
one = 1
for i in range(N):
    S, B = map(int, input().split())
    food_list_S.append(S)
    food_list_B.append(B)
for j in range(N):
    one *= food_list_S[j]
result = one - sum(food_list_B)
print(abs(result))


4
1 7
2 6
3 8
4 9
'''