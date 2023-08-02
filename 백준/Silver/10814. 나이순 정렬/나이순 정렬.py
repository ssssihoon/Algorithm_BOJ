N = int(input())

li = []

for i in range(N):
    a, b = input().split()
    li.append([int(a), i, b])
li.sort()

for i in range(N):
    print(li[i][0], li[i][2])