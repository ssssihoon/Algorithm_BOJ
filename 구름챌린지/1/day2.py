N = int(input())
T, M = map(int, input().split())
C = [int(input()) for i in range(N)]
M = M+sum(C)
while M >= 60:
    T += 1
    if T >= 24:
        T = 0
    M -= 60

print(T, M)