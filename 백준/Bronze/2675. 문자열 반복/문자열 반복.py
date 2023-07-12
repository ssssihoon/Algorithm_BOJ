T = int(input())
for i in range(T):
    S = input().split()
    R = int(S[0])
    list_S = list(S[1])
    for j in list_S:
        print(R*j, end = "")
    print()


'''
2
3 ABC
5 /HTP   
'''