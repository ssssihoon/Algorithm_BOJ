num = int(input()) # 정수형 입력값을 num이라는 변수에 저장
for i in range(num, 0, -1): # for문 num 수 부터  1까지 가감
    print('*' * i) # 문자 '*'에 i의 곱(n, n-1, n-2, ''')
