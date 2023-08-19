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

N, K = list(map(int, input().split()))

li = list(map(int, input().split()))


for i in range(N):
    binarynumber = bin(li[i])[2:]

    count = 0
    for c in binarynumber:
        if c == '1':
            count += 1
    result.append([count, li[i]])

result.sort(reverse=True)

print(result[K-1][1])
