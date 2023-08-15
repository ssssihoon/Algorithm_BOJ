import sys

input = sys.stdin.readline


W , R = map(int, input().split())

Onerm = W*(1+R/30)
print(int(Onerm))