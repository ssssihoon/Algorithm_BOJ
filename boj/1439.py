S = list(input())
a = "0"
count_a = 0
count_b = 0

for i in S:
    if i != "0":
        if i != a:
            count_a += 1
    a = i

for i in S:
    if i != "1":
        if i != a:
            count_b += 1
    a = i
if count_a >= count_b:
    print(count_b)
else:
    print(count_a)
