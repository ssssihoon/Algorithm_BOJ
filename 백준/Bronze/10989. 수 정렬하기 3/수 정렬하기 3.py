import sys
input = sys.stdin.readline


N = int(input())

li = [0] * 10001 #이 수는 10,000보다 작거나 같은 자연수이다.

for i in range(N):
    li[int(input())] += 1 # 받은 숫자의 위치에 1을 더함, 2이면 두번 출력하게

for i in range(10001):
    if li[i] != 0: #0이 아닐 때
        for j in range(li[i]): #있으면 숫자만큼
            print(i)

