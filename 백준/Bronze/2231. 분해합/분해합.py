
sum_n_count = 0

N = int(input())
for i in range(1, N+1):
    num = sum((map(int, str(i))))
    sum_n_count = i + num
    if sum_n_count == N:
        print(i)
        break
    if i == N:
        print(0)