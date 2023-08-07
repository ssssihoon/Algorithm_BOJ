str_num = input()

while str_num[0] != "0":
    if str_num == str_num[::-1]:
        print("yes")
        str_num = input()
    else:
        print("no")
        str_num = input()


