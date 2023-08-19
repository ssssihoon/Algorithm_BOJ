import sys
input = sys.stdin.readline

N = int(input())

li = []
result = []
for i in range(N):
    a, b = (input().split())
    li.append([int(a), int(b)])

li.sort()
for i in li:
    print(*(i))
