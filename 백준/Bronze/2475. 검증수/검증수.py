nums = input().split()
sq_sum = 0
for i in range(len(nums)):
    sq_sum += int(nums[i])**2
print(sq_sum % 10)