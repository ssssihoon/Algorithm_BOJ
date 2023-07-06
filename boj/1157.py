Word = input().lower() # Word 에 대문자를 넣는 입력값을 생각하여 모두 소문자화
Word_list = list(set(Word)) #set() 을 사용하여 자료형의 중복 제거후 리스트로 넣음
cnt = [] #cnt라는 리스트 변수 선언 ->count , 초기화

for i in Word_list: #Word_list 안의 문자들을 for문으로 반복
    count = Word.count(i) #Word안의 그 문자가 몇개인지 count
    cnt.append(count) #cnt 변수리스트에 append. / cnt = [4, 4, 1, 1]

if cnt.count(max(cnt)) >= 2: #max(cnt)의 값 [가장큰 값]을 가지는 것이 2개 이상이라면
    print("?") #"?"출력
else:
    print(Word_list[(cnt.index(max(cnt)))].upper())  #index() 함수 -> 값의 위치를 찾아주는 함수
    #Word = baaa , Word_list = [b, a], cnt = [1, 3]
    #max(cnt)는 3이되고, index(3)은 cnt에서 cnt[1]에 위치하기 때문에
    # 즉, index자체가 가리키는 3이 cnt[1]이기 때문에 Word_list[1]은 a를 가리키는데
    # 이것이 upper로 인해 대문자로만 출력되기때문에 A가 출력됨

