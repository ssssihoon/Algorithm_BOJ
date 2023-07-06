a = int(input())
b = list(input())
B = "".join(b)

b_2 = b[2]
b_1 = b[1]
b_0 = b[0]

print(a * int(b_2))
print(a * int(b_1))
print(a * int(b_0))
print(a * int(B))

#list_a = [int(i) for i in list_a] -> 문자형을 정수형 리스트로 변환
#str = "".join(arr) -> 리스트를 하나의 문자열로 합치기