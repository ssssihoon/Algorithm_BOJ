number = list(map(int, input().split()))
A = number[0]
B = number[1]
V = number[2]

day = (V-B) / (A-B) # A*day - B(day-1) = V
if day == int(day):
    print(int(day))
else:
    print(int(day) + 1)