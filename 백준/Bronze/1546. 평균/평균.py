import sys

N = int(sys.stdin.readline())
scores = list(map(int, sys.stdin.readline().split()))
max_score = max(scores)
li = []
for i in scores:
    li.append(i/max_score*100)
avg = sum(li)/N
print(avg)
