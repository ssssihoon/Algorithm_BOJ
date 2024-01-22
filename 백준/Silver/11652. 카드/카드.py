'''
많은 것 출력
만약 많은 것이 여러개라면 작은 것 출력
'''

import sys

input = sys.stdin.readline

n = int(input())

dict = {}

for i in range(n):
    num = int(input())
    if num in dict:
        dict[num] += 1
    else:
        dict[num] = 1

count = max(dict.values())

max_li = [k for k, v in dict.items() if v == count]
max_li.sort()
print(max_li[0])
