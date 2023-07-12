li=[]
for i in range(10):
    num = int(input())
    li.append(num % 42)
print(len(set(li)))