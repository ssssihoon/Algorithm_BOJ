'''
햄버거의 맛은 사용된 모든 재료의 맛의 정도를 더한 값이다.
완벽한 햄버거 -> 맛의 정도가 가장 높은 재료를 기준으로 위랑 아래로 갈수록 재료의 맛의 정도가 감소하거나 같아야 한다.
'''

'''
7
1 2 3 5 3 1 3
'''
import sys

input = sys.stdin.readline

N = int(input())
k = list(map(int, input().split()))
sum_flavor = sum(k)
max_k = max(k)

for i in range(N):
    if i+1 < N and max_k >= k[i] and max_k != k[0] and max_k != k[-1]:
        if k[i] <= k[i+1] and max_k >= k[i]:
            continue
        elif k[i] >= k[i+1] and max_k <= k[i]:
            continue
        else:
            sum_flavor = 0
            pass
print(sum_flavor)

'''
처음과 마지막의 재료가 max값이면 안된다.
max_k != k[0] and max_k != k[-1]
'''