import sys
num_count = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(0, num_count)]
numbers.sort()
for i in numbers:
    print(i)

#input() -> 시간초과 , sys.stdin.readline() -> (O)
