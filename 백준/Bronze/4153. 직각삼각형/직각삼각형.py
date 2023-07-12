while True:
    nums = list(map(int, input().split()))
    nums.sort()
    a = nums[0]
    b = nums[1]
    c = nums[2]
    if a == 0 and b == 0 and c == 0:
        break
    if c**2 == (a**2 + b**2):
        print("right")
    else:
        print("wrong")
