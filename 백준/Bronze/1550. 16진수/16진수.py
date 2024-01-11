n_16 = list(input())

result = 0

for i in range(len(n_16)):
    if 65 <= ord(n_16[i]) <= 70:
        result += ((ord(n_16[i]) - 55) * (16 ** (len(n_16) - (i+1))))
    elif 48 <= ord(n_16[i]) <= 57:
        result += ((ord(n_16[i]) - 48) * (16 ** (len(n_16) - (i+1))))

print(result)


