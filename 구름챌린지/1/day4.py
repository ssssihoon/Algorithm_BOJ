import sys

input = sys.stdin.readline

N = int(input())
k = list(map(int, input().split()))
sum_flavor = sum(k)
max_k = max(k)
turn = 0

for i in range(N):
    if i+1 < N :
        if k[0] == max_k:
            turn = 1
        if k[i] <= k[i+1] and turn == 0:
            if k[i+1] == max_k:
                turn = 1
            continue
        elif k[i] >= k[i+1] and turn == 1:
            continue
        else:
            sum_flavor = 0
            break
print(sum_flavor)
