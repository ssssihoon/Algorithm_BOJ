H, M = list(map(int, input().split()))
if H > 0 and M < 45:
    H -= 1
    M += 15

elif H >= 0 and M >= 45:
    M -= 45

elif H == 0 and M < 45:
    H = 23
    M += 15

print(H, M)