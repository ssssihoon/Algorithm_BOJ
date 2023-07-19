import sys

N = int(sys.stdin.readline())
li = []
for i in range(N):
    str = sys.stdin.readline().split()
    if str[0] == "push":
        li.append(str[1])
    elif str[0] == "pop" :
        if len(li) == 0:
            print(-1)
        else:
            print(li.pop())
    elif str[0] == "top" :
        if len(li) == 0:
            print(-1)
        else:
            print(li[-1])
    elif str[0] == "size":
        print(len(li))
    elif str[0] == "empty" :
        if len(li) == 0:
            print(1)
        else:
            print(0)