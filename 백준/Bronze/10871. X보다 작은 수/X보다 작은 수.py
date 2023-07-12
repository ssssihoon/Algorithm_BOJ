N, X = list(map(int, input().split()))
nums = input().split()
result = ""
for i in nums:
    int_num = int(i)
    if int_num < X:
        result =  result + str(int_num) + " "
print(result)