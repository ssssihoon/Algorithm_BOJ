N = int(input())

count = 0

nums = list(map(int, input().split()))

for i in nums:
    for j in range(2, i+1):
        if i % j == 0:
            if i == j:
                count += 1
            break
print(count)