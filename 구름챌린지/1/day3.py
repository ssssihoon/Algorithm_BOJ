T = int(input())
result = 0
for i in range(T):
    ex = input().split()
    int1 = int(ex[0])
    int2 = int(ex[2])
    calculation = ex[1]

    if calculation == '+':
        result += int1 + int2
    elif calculation == '-':
        result += int1 - int2
    elif calculation == '/':
        result += int1 // int2
    elif calculation == '*':
        result += int1 * int2
print(result)