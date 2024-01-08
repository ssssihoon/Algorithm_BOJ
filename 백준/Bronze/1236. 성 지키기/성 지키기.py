all_li = []
cnt_x = 0
cnt_y = 0

n, m = map(int, input().split())
row_cnt_a = [0]*m
row_cnt_b = [0]*m
cnt_li_a = [[0]*m]*n
cnt_li_b = [[0]*m]*n

for y in range(n):
    li = list(input())
    all_li.append(li)
    for x in range(m):
        if all_li[y][x] == 'X':
            row_cnt_a[x] += 1
    if sum(row_cnt_a) == 0:
        cnt_x += 1
    row_cnt_a = [0]*m


for y in range(m):
    for x in range(n):
        if all_li[x][y] == 'X':
            row_cnt_b[y] += 1
    if sum(row_cnt_b) == 0:
        cnt_y += 1
    row_cnt_b = [0]*m

print(max(cnt_x, cnt_y))