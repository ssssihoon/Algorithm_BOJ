import sys
input = sys.stdin.readline

N = int(input())

li = []
result = []
for i in range(N):
    a, b = (input().split())
    li.append([int(b), int(a)])

li.sort()

for y in li:
    print(*y[::-1])
