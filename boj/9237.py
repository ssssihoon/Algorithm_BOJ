n = int(input())

tree_day = list(map(int, input().split()))
tree_day.sort()
tree_day_reverse = tree_day[::-1]

for i in range(n):
    tree_day_reverse[i] = tree_day_reverse[i] + i + 1
print(max(tree_day_reverse) + 1)

# tree_day_reverse[i] = tree[i] + i + 1
# 값 = 나무가 자라는 시간 + 몇번째 나무를 심는지 + 나무 심는데 하루
"""
묘목을 구입한 날 date-> +1
묘목하나를 심는데 걸리는 시간-> +1일
자라는 시간  = tree_day
마지막 나무가 다 자란 다음날 이장님을  초대 invite -> + 1일
"""
