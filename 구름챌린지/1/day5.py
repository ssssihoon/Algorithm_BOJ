# 리스트 두개를 대응시켜 정렬하는 부분을 모르겠다.
# 리스트 두개를 대응시켜 정렬하는 부분을 모르겠다.
# 리스트 두개를 대응시켜 정렬하는 부분을 모르겠다.
# 리스트 두개를 대응시켜 정렬하는 부분을 모르겠다.
# 리스트 두개를 대응시켜 정렬하는 부분을 모르겠다.



'''
N : 10진수의 개수, K : 찾으려는 정수의 위치, a : 정수

First, 2진수에 포함된 1의 개수를 기준으로 내림차순 정렬

Second, 1의 개수가 같다면, 10진수를 기준으로 내림차순 정렬

Third, K번째 위치한 수는 어떤 수일지

ex : ) 1의 개수대로 내림차순 정렬을 해야하는게 우선이다. 그때의 K번째는 어떤 것인가
'''

empty = []
one_count = []
result = []
N ,K = list(map(int, input().split()))

li = list(map(int, input().split()))

for i in range(N):
    li_to_bin = bin(li[i])
    empty.append(int(li_to_bin[2:]))  #empty라는 변수는 2진수로 변환한 정수값이다.
    
for j in empty:
    str_j = str(j)
    one_count.append(str_j.count("1")) # 1의 개수를 세어준다.
    
print(empty)
print(one_count)

for m, n in zip(empty, one_count):
    print(m, n)
