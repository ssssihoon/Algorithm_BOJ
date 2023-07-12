S = list(map(int, input().split()))
up = [1, 2, 3, 4, 5, 6, 7, 8]
down = [8, 7, 6, 5, 4, 3, 2, 1]
if S == up:
    print("ascending")
elif S == down:
    print("descending")
else:
    print("mixed")