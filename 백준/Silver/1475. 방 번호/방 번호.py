num_cnt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
room_number = list(map(int, input()))

for i in room_number:
     if i == 6 or i == 9:
        if num_cnt[6] < num_cnt[9]:
            num_cnt[6] += 1
        elif num_cnt[6] > num_cnt[9]:
            num_cnt[9] += 1
        else :
            num_cnt[i] += 1
     else:
        num_cnt[i] += 1
print(max(num_cnt))