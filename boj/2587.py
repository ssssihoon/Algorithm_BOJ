numbers = [int(input()) for _ in range(5)] #5개의 입력값을 받는 정수형 리스트 numbers 선언
numbers.sort() #numbers리스트 오름차순 정렬

print(round(sum(numbers) / 5)) #numbers리스트 합)/5
print(numbers[2]) #numbers리스트 안의 3번째 값 출력